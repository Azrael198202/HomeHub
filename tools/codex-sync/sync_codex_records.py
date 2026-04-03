from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import shutil
import socket
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = Path(os.environ.get("CODEX_SYNC_CONFIG", SCRIPT_DIR / "codex-sync.config.json"))


@dataclass
class SyncConfig:
    source_dir: Path
    repo_dir: Path
    machine_name: str
    branch: str
    target_root: str
    delete_missing: bool
    include_patterns: list[str]
    exclude_patterns: list[str]


def load_config() -> SyncConfig:
    if not CONFIG_PATH.exists():
        example = SCRIPT_DIR / "codex-sync.config.example.json"
        fail(
            "Missing config file.\n"
            f"Create {CONFIG_PATH.name} next to this script, based on {example.name}."
        )

    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Config file is not valid JSON: {exc}")

    source_dir = Path(raw.get("sourceDir", "")).expanduser()
    repo_dir = Path(raw.get("repoDir", "")).expanduser()
    machine_name = raw.get("machineName") or socket.gethostname()
    branch = raw.get("branch") or "main"
    target_root = raw.get("targetRoot") or "records"
    delete_missing = bool(raw.get("deleteMissing", False))
    include_patterns = list(raw.get("includePatterns") or ["**/*"])
    exclude_patterns = list(raw.get("excludePatterns") or [])

    if not source_dir.is_dir():
        fail(f"sourceDir does not exist or is not a directory: {source_dir}")
    if not repo_dir.is_dir():
        fail(f"repoDir does not exist or is not a directory: {repo_dir}")
    if not (repo_dir / ".git").exists():
        fail(f"repoDir is not a Git repository: {repo_dir}")

    return SyncConfig(
        source_dir=source_dir,
        repo_dir=repo_dir,
        machine_name=machine_name,
        branch=branch,
        target_root=target_root.strip("/\\"),
        delete_missing=delete_missing,
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
    )


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def run_git(repo_dir: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    cmd = ["git", *args]
    result = subprocess.run(
        cmd,
        cwd=repo_dir,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "unknown git error"
        fail(f"Git command failed: {' '.join(cmd)}\n{details}")
    return result


def normalize_rel_path(path: Path) -> str:
    return path.as_posix()


def matches_any(path_text: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path_text, pattern) for pattern in patterns)


def should_copy(rel_path: Path, include_patterns: list[str], exclude_patterns: list[str]) -> bool:
    path_text = normalize_rel_path(rel_path)
    if not matches_any(path_text, include_patterns):
        return False
    if matches_any(path_text, exclude_patterns):
        return False
    return True


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_source_files(source_dir: Path, include_patterns: list[str], exclude_patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for path in source_dir.rglob("*"):
        if not path.is_file():
            continue
        rel_path = path.relative_to(source_dir)
        if should_copy(rel_path, include_patterns, exclude_patterns):
            files.append(rel_path)
    return sorted(files)


def sync_files(config: SyncConfig) -> tuple[int, int]:
    target_dir = config.repo_dir / config.target_root / config.machine_name
    target_dir.mkdir(parents=True, exist_ok=True)

    source_files = collect_source_files(config.source_dir, config.include_patterns, config.exclude_patterns)
    copied = 0

    for rel_path in source_files:
        source_path = config.source_dir / rel_path
        destination_path = target_dir / rel_path
        destination_path.parent.mkdir(parents=True, exist_ok=True)

        if destination_path.exists() and sha256(source_path) == sha256(destination_path):
            continue

        shutil.copy2(source_path, destination_path)
        copied += 1

    deleted = 0
    if config.delete_missing:
        current_set = {normalize_rel_path(path) for path in source_files}
        for path in sorted(target_dir.rglob("*"), reverse=True):
            if not path.is_file():
                continue
            rel_path = normalize_rel_path(path.relative_to(target_dir))
            if rel_path == ".codex-sync-meta.json":
                continue
            if rel_path not in current_set:
                path.unlink()
                deleted += 1

        remove_empty_dirs(target_dir)

    write_metadata(config, target_dir, source_files)
    return copied, deleted


def remove_empty_dirs(root: Path) -> None:
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def write_metadata(config: SyncConfig, target_dir: Path, source_files: list[Path]) -> None:
    metadata = {
        "machineName": config.machine_name,
        "sourceDir": str(config.source_dir),
        "syncedAtUtc": datetime.now(timezone.utc).isoformat(),
        "fileCount": len(source_files),
        "branch": config.branch,
    }
    meta_path = target_dir / ".codex-sync-meta.json"
    meta_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def ensure_clean_git_state(repo_dir: Path) -> None:
    status = run_git(repo_dir, "status", "--porcelain", check=True)
    if status.stdout.strip():
        fail(
            "Target repository has uncommitted changes.\n"
            "Commit or stash them before running the sync tool."
        )


def main() -> None:
    config = load_config()
    ensure_clean_git_state(config.repo_dir)

    print(f"Syncing from: {config.source_dir}")
    print(f"Syncing into: {config.repo_dir}")
    print(f"Machine name: {config.machine_name}")
    print(f"Branch: {config.branch}")

    run_git(config.repo_dir, "checkout", config.branch)
    run_git(config.repo_dir, "pull", "--rebase", "origin", config.branch)

    copied, deleted = sync_files(config)

    run_git(config.repo_dir, "add", "--all")
    status = run_git(config.repo_dir, "status", "--porcelain")
    if not status.stdout.strip():
        print("No changes to commit.")
        return

    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"sync: {config.machine_name} {timestamp}"
    run_git(config.repo_dir, "commit", "-m", commit_message)
    run_git(config.repo_dir, "push", "origin", config.branch)

    print(f"Sync complete. Copied: {copied}, Deleted: {deleted}")


if __name__ == "__main__":
    main()
