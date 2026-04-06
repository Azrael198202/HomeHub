#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR"

sh ./pull_codex_records.sh

HANDOFF_PATH="${CODEX_HANDOFF_PATH:-$HOME/.codex/handoff.md}"

if [ ! -f "$HANDOFF_PATH" ]; then
  echo "No handoff file found at: $HANDOFF_PATH"
  echo "On the other machine, run: Generate And Sync Codex Handoff"
  exit 0
fi

echo "Handoff ready: $HANDOFF_PATH"

if command -v pbcopy >/dev/null 2>&1; then
  pbcopy < "$HANDOFF_PATH"
  echo "Handoff content copied to clipboard."
fi

if [ "${CODEX_NO_OPEN:-0}" != "1" ] && command -v open >/dev/null 2>&1; then
  open "$HANDOFF_PATH"
fi

echo "Paste clipboard content into the new chat to continue."
