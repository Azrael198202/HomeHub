@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_BIN="
where py >nul 2>nul
if %errorlevel%==0 (
  set "PYTHON_BIN=py -3"
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    set "PYTHON_BIN=python"
  )
)

if not defined PYTHON_BIN (
  echo Python 3 was not found. Install Python 3 and try again.
  exit /b 1
)

%PYTHON_BIN% generate_handoff.py %*
exit /b %errorlevel%
