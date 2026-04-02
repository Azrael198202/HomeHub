$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir
$env:HOMEHUB_PORT = "8787"
Write-Host "Starting HomeHub at http://127.0.0.1:$env:HOMEHUB_PORT"
python runtime/server.py
