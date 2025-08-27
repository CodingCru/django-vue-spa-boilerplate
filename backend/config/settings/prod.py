import os

from .base import *  # noqa: F403

DEBUG = False
# ALLOWED_HOSTS must be set via env var in production
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or "unsafe-default"
if SECRET_KEY == "unsafe-default":
    raise RuntimeError("SECRET_KEY must be set in prod")
