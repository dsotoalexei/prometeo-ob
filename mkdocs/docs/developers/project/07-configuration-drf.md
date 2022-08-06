# Adicionar Django Rest Framework `DRF`

Django Rest Framework (DRF) es una herramienta que nos va a facilitar el desarrollo de APIs para nuestra web.

## Instalar dependencias

```zsh
# Instalar paquete djangorestframework usando poetry
$> poetry add djangorestframework
```

| Nombre              | Descripción                         |
| ------------------- | ----------------------------------- |
| djangorestframework | API web para Django, simplificadas. |

## Configurar DRF

Crear fichero `drf.py` en la ubicación `src/server/settings/components/`

```python
# -- REST FRAMEWORK CONFIGURATIONS --
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
      'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication',),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',
        'user': '5000/day',
    },
}
```

Adicionar configuración en el fichero `src/config/settings/__init__.py`

```python
base_settings = [
    ...
    'components/drf.py',
    ...
]
```

Adicionar configuración en el fichero `src/config/settings/components/common.py`

```python
# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    ...
    # API REST:
    'rest_framework',
)
```

## Bibliografía

- [Web Oficil](https://www.django-rest-framework.org/)
- [Ejemplo 1](http://blog.enriqueoriol.com/2014/06/introduccion-django-rest-framework.html)
- [Ejemplo APIViews](https://testdriven.io/blog/drf-views-part-1/)
- [Ejemplo Generic Views](https://testdriven.io/blog/drf-views-part-2/)
- [Ejemplo ViewSets](https://testdriven.io/blog/drf-views-part-3/)
