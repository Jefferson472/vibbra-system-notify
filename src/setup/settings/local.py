from .base import *


DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DJANGO-DEBUG-TOOLBAR CONFIGURATION
if config("DJANGO_TOOLBAR", cast=bool, default=False):
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

    INSTALLED_APPS += ("debug_toolbar",)

    # IPs allowed to see django-debug-toolbar output.
    INTERNAL_IPS = ("127.0.0.1",)

    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
        "SHOW_TEMPLATE_CONTEXT": True,
        "HIDE_DJANGO_SQL": True,
    }
