@echo off
setlocal
cd /d "%~dp0"

if not exist "codex-sync.config.json" (
  if exist "codex-sync.config.example.json" (
    copy /Y "codex-sync.config.example.json" "codex-sync.config.json" >nul
    echo Created codex-sync.config.json from template.
    echo Please edit codex-sync.config.json, then run again.
    exit /b 1
  ) else (
    echo Missing both codex-sync.config.json and codex-sync.config.example.json.
    exit /b 1
  )
)

where git >nul 2>nul
if not %errorlevel%==0 (
  echo Git was not found. Trying to install with winget...
  winget install --id Git.Git -e --silent --accept-source-agreements --accept-package-agreements
  where git >nul 2>nul
  if not %errorlevel%==0 (
    echo Git installation failed. Install Git and try again.
    exit /b 1
  )
)

set "PYTHON_BIN="
where py >nul 2>nul
if %errorlevel%==0 (
  set "PYTHON_BIN=py -3"
) else (
  where python >nul 2>nul
  if %errorlevel%==0 (
    set "PYTHON_BIN=python"
  ) else (
    echo Python 3 was not found. Trying to install with winget...
    winget install --id Python.Python.3 -e --silent --accept-source-agreements --accept-package-agreements
    where py >nul 2>nul
    if %errorlevel%==0 (
      set "PYTHON_BIN=py -3"
    ) else (
      where python >nul 2>nul
      if %errorlevel%==0 (
        set "PYTHON_BIN=python"
      )
    )
  )
)

if not defined PYTHON_BIN (
  echo Python 3 was not found. Install Python 3 and try again.
  exit /b 1
)

%PYTHON_BIN% pull_codex_records.py
set "EXIT_CODE=%errorlevel%"

if not "%EXIT_CODE%"=="0" (
  echo.
  echo Import failed with exit code %EXIT_CODE%.
)

exit /b %EXIT_CODE%
