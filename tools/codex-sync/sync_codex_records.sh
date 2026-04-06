#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR"

ensure_brew() {
  if command -v brew >/dev/null 2>&1; then
    return 0
  fi
  echo "Homebrew is required for automatic install on macOS."
  echo "Install it from: https://brew.sh"
  return 1
}

ensure_git() {
  if command -v git >/dev/null 2>&1; then
    return 0
  fi
  if ! ensure_brew; then
    return 1
  fi
  echo "Installing git via Homebrew..."
  brew install git
}

ensure_python3() {
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
    return 0
  fi
  if command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
    return 0
  fi
  if ! ensure_brew; then
    return 1
  fi
  echo "Installing python via Homebrew..."
  brew install python
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
    return 0
  fi
  echo "Python 3 install completed but python3 is still unavailable."
  return 1
}

ensure_config() {
  if [ -f "codex-sync.config.json" ]; then
    return 0
  fi
  if [ ! -f "codex-sync.config.example.json" ]; then
    echo "Missing both codex-sync.config.json and codex-sync.config.example.json."
    return 1
  fi
  cp "codex-sync.config.example.json" "codex-sync.config.json"
  echo "Created codex-sync.config.json from template."
  echo "Please edit codex-sync.config.json, then run again."
  return 1
}

ensure_git
ensure_python3
ensure_config

"$PYTHON_BIN" sync_codex_records.py
