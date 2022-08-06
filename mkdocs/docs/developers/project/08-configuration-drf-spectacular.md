# Documentar API con DRF  Spectacular

## Instalar dependencias

```zsh
$> poetry add drf-spectacular
```

| Nombre          | Descripción                                                  |
| --------------- | ------------------------------------------------------------ |
| drf-spectacular | Generación de esquemas OpenAPI 3 sensato y flexible para el marco Django REST |

## Configurar DRF Spectacular

Editar el fichero `drf.py` en la ubicación `src/server/settings/components/`

```python
# -- REST FRAMEWORK CONFIGURATIONS --
REST_FRAMEWORK = {
    ...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    ...
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}
```

Adicionar configuración en el fichero `src/server/settings/components/common.py`

```python
# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    ...

  	# DRF Spectacular:
    'drf_spectacular',
)
```

Editar el fichero `urls.py` en la ubicación `src/server`

```python
"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # API Documentation
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
]
```

## Bibliografía

- [Información del paquete](https://drf-spectacular.readthedocs.io/en/latest/readme.html)
- [Ejemplo](https://rohitkrgupta.medium.com/swagger-with-django-made-easy-a-drf-spectacular-explainer-20b18bb4c33c)
- [Ejemplo de uso](https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje)
