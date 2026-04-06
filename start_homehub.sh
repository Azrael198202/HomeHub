#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"
export HOMEHUB_PORT="${HOMEHUB_PORT:-8787}"

echo "Starting HomeHub at http://127.0.0.1:${HOMEHUB_PORT}"
python3 runtime/server.py
