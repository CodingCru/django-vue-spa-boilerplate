import os

env = os.getenv("DJANGO_ENV", "dev").lower()

if env == "prod":
    from .prod import *  # noqa: F401,F403
elif env == "staging":
    from .staging import *  # noqa: F401,F403
else:
    from .dev import *  # noqa: F403

SETTINGS_ENV = env  # handy for diagnostics
