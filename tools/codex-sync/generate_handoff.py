from __future__ import annotations

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = Path(os.environ.get("CODEX_SYNC_CONFIG", SCRIPT_DIR / "codex-sync.config.json"))
FALLBACK_SOURCE_DIR = Path.home() / ".codex"


def find_latest_session(sessions_root: Path) -> Path:
    files = sorted(p for p in sessions_root.rglob("*.jsonl") if p.is_file())
    if not files:
        raise SystemExit(f"No session files found under: {sessions_root}")
    return files[-1]


def parse_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def extract_text_content(content: Any) -> str:
    if not isinstance(content, list):
        return ""
    chunks: list[str] = []
    for item in content:
        if not isinstance(item, dict):
            continue
        text = item.get("text")
        if isinstance(text, str) and text.strip():
            chunks.append(text.strip())
    return "\n".join(chunks).strip()


def compress_line(text: str, limit: int = 220) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def extract_patch_files(patch_text: str) -> list[str]:
    matches = re.findall(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", patch_text, re.MULTILINE)
    cleaned = [m.strip() for m in matches if m.strip()]
    return cleaned


def unique_keep_order(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        out.append(item)
    return out


def load_sync_config_source_dir() -> Path:
    if not CONFIG_PATH.exists():
        return FALLBACK_SOURCE_DIR
    try:
        raw = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return FALLBACK_SOURCE_DIR
    value = raw.get("sourceDir")
    if not isinstance(value, str) or not value.strip():
        return FALLBACK_SOURCE_DIR
    return Path(value).expanduser()


def resolve_sessions_root(source_dir: Path) -> Path:
    env_value = os.environ.get("CODEX_SESSIONS_DIR")
    if env_value:
        return Path(env_value).expanduser()
    return source_dir / "sessions"


def resolve_output_path(source_dir: Path) -> Path:
    env_value = os.environ.get("CODEX_HANDOFF_OUT")
    if env_value:
        return Path(env_value).expanduser()
    return source_dir / "handoff.md"


def build_handoff(records: list[dict[str, Any]], session_path: Path) -> str:
    session_id = ""
    session_cwd = ""
    session_time = ""
    user_messages: list[str] = []
    assistant_finals: list[str] = []
    file_changes: list[str] = []
    command_calls: list[str] = []

    for record in records:
        record_type = record.get("type")
        payload = record.get("payload")

        if record_type == "session_meta" and isinstance(payload, dict):
            session_id = str(payload.get("id") or session_id)
            session_cwd = str(payload.get("cwd") or session_cwd)
            session_time = str(payload.get("timestamp") or session_time)
            continue

        if not isinstance(payload, dict):
            continue

        if record_type == "event_msg" and payload.get("type") == "user_message":
            message = payload.get("message")
            if isinstance(message, str) and message.strip():
                user_messages.append(message.strip())
            continue

        if record_type == "event_msg" and payload.get("type") == "agent_message":
            if payload.get("phase") == "final_answer":
                message = payload.get("message")
                if isinstance(message, str) and message.strip():
                    assistant_finals.append(message.strip())
            continue

        if record_type != "response_item":
            continue

        payload_type = payload.get("type")
        if payload_type == "message":
            role = payload.get("role")
            if role == "user":
                text = extract_text_content(payload.get("content"))
                if text:
                    user_messages.append(text)
            elif role == "assistant" and payload.get("phase") == "final_answer":
                text = extract_text_content(payload.get("content"))
                if text:
                    assistant_finals.append(text)
            continue

        if payload_type == "function_call":
            name = payload.get("name")
            args_raw = payload.get("arguments")
            if name == "exec_command" and isinstance(args_raw, str):
                try:
                    parsed = json.loads(args_raw)
                except json.JSONDecodeError:
                    parsed = {}
                cmd = parsed.get("cmd")
                if isinstance(cmd, str) and cmd.strip():
                    command_calls.append(cmd.strip())
            continue

        if payload_type == "custom_tool_call":
            name = payload.get("name")
            if name == "apply_patch":
                patch_text = payload.get("input")
                if isinstance(patch_text, str):
                    file_changes.extend(extract_patch_files(patch_text))

    user_messages = unique_keep_order(user_messages)
    assistant_finals = unique_keep_order(assistant_finals)
    file_changes = unique_keep_order(file_changes)
    command_calls = unique_keep_order(command_calls)

    top_user = [compress_line(msg) for msg in user_messages[-8:]]
    top_assistant = [compress_line(msg) for msg in assistant_finals[-5:]]
    top_commands = [compress_line(cmd, 180) for cmd in command_calls[-12:]]

    generated_at = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    session_rel = session_path.as_posix()

    lines: list[str] = [
        "# Codex Handoff",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Source session: `{session_rel}`",
        f"- Session id: `{session_id or 'unknown'}`",
        f"- Session time: `{session_time or 'unknown'}`",
        f"- Workspace: `{session_cwd or 'unknown'}`",
        "",
        "## User Requests (Recent)",
    ]

    if top_user:
        lines.extend(f"- {item}" for item in top_user)
    else:
        lines.append("- (none found)")

    lines.append("")
    lines.append("## Assistant Outcomes (Recent)")
    if top_assistant:
        lines.extend(f"- {item}" for item in top_assistant)
    else:
        lines.append("- (none found)")

    lines.append("")
    lines.append("## Files Touched")
    if file_changes:
        lines.extend(f"- `{path}`" for path in file_changes)
    else:
        lines.append("- (no apply_patch file changes found)")

    lines.append("")
    lines.append("## Commands Used (Recent)")
    if top_commands:
        lines.extend(f"- `{cmd}`" for cmd in top_commands)
    else:
        lines.append("- (none found)")

    lines.append("")
    lines.append("## Continue Prompt")
    lines.append(
        "- Continue from this handoff. First verify current repo state, then resume the latest unfinished task."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    source_dir = load_sync_config_source_dir()
    sessions_root = resolve_sessions_root(source_dir)
    output_path = resolve_output_path(source_dir)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    session_path = find_latest_session(sessions_root)
    records = parse_jsonl(session_path)
    handoff = build_handoff(records, session_path)
    output_path.write_text(handoff, encoding="utf-8")
    print(f"Handoff generated: {output_path}")


if __name__ == "__main__":
    main()
