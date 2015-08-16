"""
Django settings for ddrbass project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import json

from django.core.exceptions import ImproperlyConfigured

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("ddrbass")
SECRETS_FILE = str(ROOT_DIR.path("secrets.json"))
env = environ.Env()

# SECRETS CONFIGURATION
# ------------------------------------------------------------------------------
with open(str(ROOT_DIR.path("secrets.json"))) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """
    Get the secret config setting or raise an ImproperlyConfigured exception
    """
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured(
            "Setting '%s' was not found in '%s'" % (setting, SECRETS_FILE)
        )


SECRET_KEY = get_secret("SECRET_KEY")

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)
THIRD_PARTY_APPS = (
)
# Apps specific for this project go here
LOCAL_APPS = (
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
)

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
# TODO

# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
DEBUG = False

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# TODO

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = (
    ("""Nathan Chowning""", "nathan@chowning.me"),
)
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# TODO Switch to mysql config
# TODO Pull this from secret json file
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR.path("db.sqlite3")),
    }
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
# SITE_ID = 1  # TODO What is this
USE_I18N = True
USE_L10N = True
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR("static"))
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    str(APPS_DIR.path("static")),
)

# URL CONFIGURATION
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"