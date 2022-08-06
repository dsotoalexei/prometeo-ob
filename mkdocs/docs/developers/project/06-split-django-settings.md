# Dividir las configuraciones de Django

## Instalar dependencias

```zsh
$> poetry add django-split-settings python-decouple structlog
```

| Nombre                                                       | Descripción                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [django-split-settings](https://django-split-settings.readthedocs.io/en/stable/) | Organice la configuración de Django en varios archivos y directorios. Anule y modifique fácilmente la configuración. Utilice comodines y archivos de configuración opcionales. |
| [python-decouple](https://pypi.org/project/python-decouple/) | Paquete de Python diseñado para separar la configuración del resto del código de su proyecto y, en el proceso, proteger sus claves secretas y otras variables. |
| [structlog](https://www.structlog.org/)                      | structlog hace que iniciar sesión en Python sea más rápido, menos doloroso y más poderoso al agregar estructura a sus entradas de registro. |

## Crear estructura

```zsh
src
└── server
    ├── __init__.py
    ├── apps
    │   └── __init__.py
    ├── asgi.py
    ├── settings
    │   ├── __init__.py
    │   ├── apps
    │   │   └── __init__.py
    │   ├── components
    │   │   ├── __init__.py
    │   │   ├── caches.py
    │   │   ├── common.py
    │   │   ├── database.py
    │   │   └── logging.py
    │   └── environments
    │       ├── __init__.py
    │       ├── development.py
    │       ├── local.py
    │       ├── local.py.template
    │       └── production.py
    ├── urls.py
    └── wsgi.py
```

- En el directorio **`src/server/apps`**, se encuentran las aplicaciones de Django, en caso de utlizar alguna variable de configuración para esa aplicación se debería definir dentro del directorio **`src/server/settings/apps`**.
- En el directorio **`src/server/settings`** se guardan todas las configuraciones relacionadas con el proyecto:
  - **`src/server/settings/apps`**: Se ponen las configuraciones para cada aplicación.
  - **`src/server/settings/components`**: Se definen las configuraciones del Framework Django así como paquetes de terceros.
  - **`src/server/settings/enviroments`**: Acá se define la configuración de los diferentens ambientes de trabajo.

> **NOTA**
>
> La configuracíon de las variables de entorno se obtienen del directorio **`config/.env`**

### Configuración de cada fichero

- `settings/__init__.py`

```python
"""
This is a django-split-settings main file.

For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings

To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""

from os import environ

from split_settings.tools import include, optional # type: ignore

# Managing environment via `DJANGO_ENV` variable:
environ.setdefault('DJANGO_ENV', 'development')
_ENV = environ['DJANGO_ENV']

_base_settings = (
    'components/common.py', # standard django settings
    'components/database.py',
    'components/caches.py',
    'components/logging.py',

    # Select the right env:
    'environments/{0}.py'.format(_ENV),

    # Optionally override some settings:
    optional('environments/local.py'),
)

# Include settings:
include(*_base_settings)
```

- `settings/components/caches.py`

```python
# Caching
# https://docs.djangoproject.com/en/3.2/topics/cache/

CACHES = {
    'default': {
        # TODO: use some other cache in production,
        # like https://github.com/jazzband/django-redis
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
```

- `settings/components/common.py`

```python
"""
Django settings for server project.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their config, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from typing import Dict, List, Tuple, Union

from django.utils.translation import gettext_lazy as _ # type: ignore

from server.settings.components import BASE_DIR, config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = config('DJANGO_SECRET_KEY')

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps go here:

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',
)

MIDDLEWARE: Tuple[str, ...] = (
    # Django:
    'django.middleware.security.SecurityMiddleware',
    # django-permissions-policy
    #'django_permissions_policy.PermissionsPolicyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.urls'

WSGI_APPLICATION = 'server.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Templates
# https://docs.djangoproject.com/en/3.2/ref/templates/api

TEMPLATES = [{
    'APP_DIRS': True,
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        # Contains plain text templates, like `robots.txt`:
        # BASE_DIR.joinpath('server', 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            # Default template context processors:
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },
}]


# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')


# Django authentication system
# https://docs.djangoproject.com/en/3.2/topics/auth/

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Security
# https://docs.djangoproject.com/en/3.2/topics/security/

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

# https://github.com/DmytroLitvinov/django-http-referrer-policy
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
REFERRER_POLICY = 'same-origin'

# https://github.com/adamchainz/django-permissions-policy#setting
PERMISSIONS_POLICY: Dict[str, Union[str, List[str]]] = {}  # noqa: WPS234


# Timeouts
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-EMAIL_TIMEOUT

EMAIL_TIMEOUT = 5


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
```

- `settings/components/database.py`

```python
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES: object = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

```

- `settings/components/logging.py`

```python
# Logging
# https://docs.djangoproject.com/en/3.2/topics/logging/

# See also:
# 'Do not log' by Nikita Sobolev (@sobolevn)
# https://sobolevn.me/2020/03/do-not-log

import structlog # type: ignore

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # We use these formatters in our `'handlers'` configuration.
    # Probably, you won't need to modify these lines.
    # Unless, you know what you are doing.
    'formatters': {
        'json_formatter': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.JSONRenderer(),
        },
        'console': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.KeyValueRenderer(
                key_order=['timestamp', 'level', 'event', 'logger'],
            ),
        },
    },

    # You can easily swap `key/value` (default) output and `json` ones.
    # Use `'json_console'` if you need `json` logs.
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
        'json_console': {
            'class': 'logging.StreamHandler',
            'formatter': 'json_formatter',
        },
    },

    # These loggers are required by our app:
    # - django is required when using `logger.getLogger('django')`
    # - security is required by `axes`
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'security': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt='iso'),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.ExceptionPrettyPrinter(),
        structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
    ],
    context_class=structlog.threadlocal.wrap_dict(dict),
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)
```

- `settings/components/__init__.py`

```python
from pathlib import Path

from decouple import AutoConfig # type: ignore

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = Path(__file__).parent.parent.parent.parent

# Loading `.env` files
# See docs: https://gitlab.com/mkleehammer/autoconfig
config = AutoConfig(search_path=BASE_DIR.joinpath('config'))
```

- `settings/enviroments/development.py`

```python
"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

# import logging
from typing import List

from server.settings.components import config
from server.settings.components.common import (
    INSTALLED_APPS,
    MIDDLEWARE,
)
from server.settings.components.database import (
    DATABASES,
)

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    'localhost',
    '0.0.0.0',  # noqa: S104
    '127.0.0.1',
    '[::1]',
]


# Installed apps for development only:

INSTALLED_APPS += (
)


# Static files:
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = []


# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io

MIDDLEWARE += (
)


# Disable persistent DB connections
# https://docs.djangoproject.com/en/3.2/ref/databases/#caveats
DATABASES['default']['CONN_MAX_AGE'] = 0  # type: ignore

```

- `settings/enviroments/production.py`

```python
"""
This file contains all the settings used in production.

This file is required and if development.py is present these
values are overridden.
"""

from server.settings.components import config

# Production flags:
# https://docs.djangoproject.com/en/3.2/howto/deployment/

DEBUG = False

ALLOWED_HOSTS = [
    # TODO: check production hosts
    config('DOMAIN_NAME'),

    # We need this value for `healthcheck` to work:
    'localhost',
]


# Staticfiles
# https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/

# This is a hack to allow a special flag to be used with `--dry-run`
# to test things locally.
_COLLECTSTATIC_DRYRUN = config(
    'DJANGO_COLLECTSTATIC_DRYRUN', cast=bool, default=False,
)
# Adding STATIC_ROOT to collect static files via 'collectstatic':
STATIC_ROOT = '.static' if _COLLECTSTATIC_DRYRUN else '/var/www/django/static'

STATICFILES_STORAGE = (
    # This is a string, not a tuple,
    # but it does not fit into 80 characters rule.
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)


# Media files
# https://docs.djangoproject.com/en/3.2/topics/files/

MEDIA_ROOT = '/var/www/django/media'


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

_PASS = 'django.contrib.auth.password_validation'  # noqa: S105
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': '{0}.UserAttributeSimilarityValidator'.format(_PASS)},
    {'NAME': '{0}.MinimumLengthValidator'.format(_PASS)},
    {'NAME': '{0}.CommonPasswordValidator'.format(_PASS)},
    {'NAME': '{0}.NumericPasswordValidator'.format(_PASS)},
]


# Security
# https://docs.djangoproject.com/en/3.2/topics/security/

SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    '^health/',
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## FAQ

### ¿Qué son las aplicaciones en Django?

Una aplicación es un conjunto portable de una funcionalidad de Django, típicamente incluye modelos y vistas, que conviven en un solo paquete de Python.

### ¿Qué es un proyecto en Django?

Un proyecto es una colección de configuraciones para una instancia de Django, incluyendo configuración de base de datos, opciones específicas de Django y configuraciones específicas de aplicaciones. Si esta es la primera vez que usas Django, tendrás que tener cuidado de algunas configuraciones iniciales.
