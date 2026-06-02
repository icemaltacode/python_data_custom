# Windows setup. Idempotent: safe to run repeatedly.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# Prefer the Python launcher (py); fall back to python on PATH.
if (Get-Command py -ErrorAction SilentlyContinue) {
  $createVenv = { py -3 -m venv .venv }
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  $createVenv = { python -m venv .venv }
} else {
  Write-Error "Python not found. Install Python 3.11+ from https://www.python.org/downloads/ (tick 'Add to PATH')."
  exit 1
}

if (-not (Test-Path ".venv")) {
  Write-Host "Creating virtual environment (.venv)..."
  & $createVenv
}

Write-Host "Installing dependencies from requirements.txt..."
& ".\.venv\Scripts\python.exe" -m pip install --upgrade pip | Out-Null
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt

Write-Host "Environment ready. In VSCode, the .venv interpreter is selected automatically."
