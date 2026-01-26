#!/usr/bin/env bash
set -euo pipefail
PY=${1:-python3}
VENV_DIR=${2:-.venv}

echo "Creating virtualenv at $VENV_DIR using $PY"
$PY -m venv "$VENV_DIR"
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel
"$VENV_DIR/bin/python" -m pip install -r requirements.txt

echo "Done. Activate with: source $VENV_DIR/bin/activate"