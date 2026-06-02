#!/usr/bin/env bash
# macOS / Linux setup. Idempotent: safe to run repeatedly.
set -e
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment (.venv)..."
  "$PY" -m venv .venv
fi

echo "Installing dependencies from requirements.txt..."
.venv/bin/python -m pip install --upgrade pip >/dev/null
.venv/bin/python -m pip install -r requirements.txt

echo "Environment ready. In VSCode, the .venv interpreter is selected automatically."
