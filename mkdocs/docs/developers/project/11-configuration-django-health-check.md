# Adicionar DJANGO HEALTH CHECK

Este proyecto verifica varias condiciones y proporciona informes cuando se detecta un comportamiento anómalo. Muchas de estas comprobaciones implican conectarse a servicios back-end y garantizar que las operaciones básicas se realicen correctamente.

## Instalar dependencias

```zsh
$> poetry add django-health-check
```

| Nombre              | Descripción |
| ------------------- | ----------- |
| django-health-check | Ejecute comprobaciones en servicios como bases de datos, servidores de cola, procesos de apio, etc.            |

## Configurar DJANGO HEALTH CHECK

Adicionar configuración en el fichero `src/server/settings/components/common.py`

```python
INSTALLED_APPS: Tuple[str, ...] = (
    ...

  	# HEALTH CHECKS:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
)
```

Adicionar configuración en el fichero `src/server/urls.py`

```python
...
from django.urls import path, include
from health_check import urls as health_urls
...

urlpatterns = [
    ...
    # Health checks:
    path("health/", include(health_urls)),
    ...
]
```

## Bibliografía

- [Documentación del paquete](https://django-health-check.readthedocs.io/en/stable/)
