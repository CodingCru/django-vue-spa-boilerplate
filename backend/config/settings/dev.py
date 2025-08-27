from .base import *  # noqa: F403

DEBUG = True
CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:5173"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
