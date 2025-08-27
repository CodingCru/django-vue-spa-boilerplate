# Django + Vue SPA Boilerplate

Minimal boilerplate for building a Django backend with a Vue 3 (Vite + TypeScript) frontend. Comes with optional Docker support and pre-configured dev tools.

## Features

- Django (API backend)
- Vue 3 + Vite + TypeScript (SPA frontend)
- Docker (for local dev or containerization)
- Pre-commit hooks (Black, Ruff, MyPy, etc.)
- Split settings (dev/prod/staging)
- Minimal, clean setup — ready to extend

## Getting Started

### Local (no Docker)

```bash
# Backend
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python manage.py migrate
python manage.py runserver

# Frontend
cd frontend
pnpm install
pnpm dev
```

### Docker (optional)

```bash
docker compose up --build
```

## Structure

```
backend/     # Django project (API)
frontend/    # Vue 3 SPA (Vite + TS)
compose.yml  # Docker Compose setup
scripts/     # (Optional) helper scripts
```

## Dev Tools

- **Linting & Formatting**: Black, Ruff
- **Typing**: MyPy + Django Stubs
- **Pre-commit hooks**
- **VS Code**: recommended settings for Python + Vue (optional)
