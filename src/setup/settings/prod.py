from .base import *


DEBUG = False

ALLOWED_HOSTS = [h.strip() for h in config("ALLOWED_HOSTS").split(",") if h.strip()]

# STATIC FILES
MIDDLEWARE += [
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}


CSRF_TRUSTED_ORIGINS = ["https://" + h for h in ALLOWED_HOSTS]
CSRF_COOKIE_SECURE = True  # cookie seguro


# MANAGER CONFIGURATION
# Admin and managers for this project. These people receive private site
# alerts.
ADMINS = ((os.environ.get("ADMIN_NAME"), os.environ.get("ADMIN_EMAIL")),)

MANAGERS = ADMINS
# END MANAGER CONFIGURATION


# EMAIL CONFIG
EMAIL_HOST = "email-ssl.com.br"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_DEFAULT_FROM", default="")


# Security
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", default=3600, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"


# ALLAUTH CONFIGURATION
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
