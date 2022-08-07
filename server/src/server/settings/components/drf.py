from django.conf import settings


# -- REST FRAMEWORK CONFIGURATIONS --
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_THROTTLE_RATES": {
        "anon": "1000/day",
        "user": "5000/day",
    },
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Prometeo OB API",
    "VERSION": "1.0.0",
    "DESCRIPTION": "API for consulting information from Prometeo.",
    "CAMELIZE_NAMES": True,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "COMPONENT_SPLIT_REQUEST": True,
    "SERVE_PERMISSIONS": ["rest_framework.permissions.AllowAny"],
    "SCHEMA_PATH_PREFIX": "/api/v[0-9]",
    'SERVE_AUTHENTICATION': None,
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_FAVICON_HREF": "assets/images/favicon.ico",
    # OTHER SETTINGS
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "filter": True,
        "displayRequestDuration": True,
        "syntaxHighlight.activate": True,
        "persistAuthorization": False,
        "syntaxHighlight.theme": "monokai",
        "displayOperationId": True,
    },
}
