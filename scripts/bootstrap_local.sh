#!/usr/bin/env bash
set -euo pipefail

# --- backend ---
cd backend
python3 -m venv .venv >/dev/null 2>&1 || true
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.sample .env
python manage.py migrate

# --- frontend ---
cd ../frontend
if command -v pnpm >/dev/null; then
  pnpm install
  pnpm approve-builds || true
else
  npm install
fi
