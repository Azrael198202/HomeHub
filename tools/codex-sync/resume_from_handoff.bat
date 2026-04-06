@echo off
setlocal
cd /d "%~dp0"

call pull_codex_records.bat
if errorlevel 1 exit /b %errorlevel%

set "HANDOFF_PATH=%USERPROFILE%\.codex\handoff.md"
if not "%CODEX_HANDOFF_PATH%"=="" set "HANDOFF_PATH=%CODEX_HANDOFF_PATH%"

if not exist "%HANDOFF_PATH%" (
  echo No handoff file found at: %HANDOFF_PATH%
  echo On the other machine, run: Generate And Sync Codex Handoff
  exit /b 0
)

echo Handoff ready: %HANDOFF_PATH%
powershell -NoProfile -Command "Get-Content -Raw '%HANDOFF_PATH%' | Set-Clipboard"
if errorlevel 1 (
  echo Clipboard copy skipped.
) else (
  echo Handoff content copied to clipboard.
)

if not "%CODEX_NO_OPEN%"=="1" (
  powershell -NoProfile -Command "Start-Process '%HANDOFF_PATH%'"
)

echo Paste clipboard content into the new chat to continue.
exit /b 0
