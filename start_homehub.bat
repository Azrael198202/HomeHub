@echo off
setlocal
cd /d "%~dp0"
set HOMEHUB_PORT=8787
echo Starting HomeHub at http://127.0.0.1:%HOMEHUB_PORT%
python runtime\server.py
endlocal
