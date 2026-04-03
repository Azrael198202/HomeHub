from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import socket
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = Path(os.environ.get("CODEX_SYNC_CONFIG", SCRIPT_DIR / "codex-sync.config.json"))


@dataclass
class PullConfig:
    source_dir: Path
    repo_dir: Path
    machine_name: str
    branch: str
    target_root: str
    include_patterns: list[str]
    exclude_patterns: list[str]
    import_from_machines: list[str]


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load_config() -> PullConfig:
    if not CONFIG_PATH.exists():
        fail(f"Missing config file: {CONFIG_PATH}")

    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Config file is not valid JSON: {exc}")

    source_dir = Path(raw.get("sourceDir", "")).expanduser()
    repo_dir = Path(raw.get("repoDir", "")).expanduser()
    machine_name = raw.get("machineName") or socket.gethostname()
    branch = raw.get("branch") or "main"
    target_root = raw.get("targetRoot") or "records"
    include_patterns = list(raw.get("includePatterns") or ["**/*", "*"])
    exclude_patterns = list(raw.get("excludePatterns") or [])
    import_from_machines = list(raw.get("importFromMachines") or [])

    if not source_dir.is_dir():
        fail(f"sourceDir does not exist or is not a directory: {source_dir}")
    if not repo_dir.is_dir():
        fail(f"repoDir does not exist or is not a directory: {repo_dir}")
    if not (repo_dir / ".git").exists():
        fail(f"repoDir is not a Git repository: {repo_dir}")

    return PullConfig(
        source_dir=source_dir,
        repo_dir=repo_dir,
        machine_name=machine_name,
        branch=branch,
        target_root=target_root.strip("/\\"),
        include_patterns=include_patterns,
        exclude_patterns=exclude_patterns,
        import_from_machines=import_from_machines,
    )


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
    for pattern in patterns:
        if fnmatch.fnmatch(path_text, pattern):
            return True
        if pattern.startswith("**/") and fnmatch.fnmatch(path_text, pattern[3:]):
            return True
    return False


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


def ensure_clean_git_state(repo_dir: Path) -> None:
    status = run_git(repo_dir, "status", "--porcelain", check=True)
    if status.stdout.strip():
        fail(
            "Target repository has uncommitted changes.\n"
            "Commit or stash them before running the import tool."
        )


def collect_repo_files(machine_dir: Path, include_patterns: list[str], exclude_patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for path in machine_dir.rglob("*"):
        if not path.is_file():
            continue
        rel_path = path.relative_to(machine_dir)
        if rel_path.name == ".codex-sync-meta.json":
            continue
        if should_copy(rel_path, include_patterns, exclude_patterns):
            files.append(rel_path)
    return sorted(files)


def load_import_state(state_path: Path) -> dict[str, str]:
    if not state_path.exists():
        return {}
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def save_import_state(state_path: Path, state: dict[str, str]) -> None:
    state_path.write_text(json.dumps(state, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def import_machine(config: PullConfig, machine_name: str, state: dict[str, str]) -> tuple[int, int, int]:
    machine_dir = config.repo_dir / config.target_root / machine_name
    if not machine_dir.is_dir():
        print(f"Skipping missing machine folder: {machine_dir}")
        return 0, 0, 0

    imported = 0
    skipped = 0
    conflicts = 0

    for rel_path in collect_repo_files(machine_dir, config.include_patterns, config.exclude_patterns):
        repo_file = machine_dir / rel_path
        local_file = config.source_dir / rel_path
        local_file.parent.mkdir(parents=True, exist_ok=True)

        key = f"{machine_name}/{normalize_rel_path(rel_path)}"
        repo_hash = sha256(repo_file)
        previous_hash = state.get(key)

        if not local_file.exists():
            local_file.write_bytes(repo_file.read_bytes())
            state[key] = repo_hash
            imported += 1
            continue

        local_hash = sha256(local_file)
        if local_hash == repo_hash:
            state[key] = repo_hash
            skipped += 1
            continue

        if previous_hash == local_hash:
            local_file.write_bytes(repo_file.read_bytes())
            state[key] = repo_hash
            imported += 1
            continue

        conflicts += 1
        print(f"Skipped locally changed file: {local_file}")

    return imported, skipped, conflicts


def main() -> None:
    config = load_config()
    ensure_clean_git_state(config.repo_dir)

    print(f"Pulling latest records from: {config.repo_dir}")
    print(f"Importing into local Codex dir: {config.source_dir}")
    if config.import_from_machines:
        print(f"Importing machine records: {', '.join(config.import_from_machines)}")
    else:
        print("No importFromMachines configured. Pull completed, import skipped.")

    run_git(config.repo_dir, "checkout", config.branch)
    run_git(config.repo_dir, "pull", "--rebase", "origin", config.branch)

    if not config.import_from_machines:
        return

    state_path = config.source_dir / ".codex-sync-import-state.json"
    state = load_import_state(state_path)

    imported = 0
    skipped = 0
    conflicts = 0
    for machine_name in config.import_from_machines:
        machine_imported, machine_skipped, machine_conflicts = import_machine(config, machine_name, state)
        imported += machine_imported
        skipped += machine_skipped
        conflicts += machine_conflicts

    save_import_state(state_path, state)
    print(f"Import complete. Imported: {imported}, Skipped: {skipped}, Conflicts: {conflicts}")


if __name__ == "__main__":
    main()
