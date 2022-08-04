# Instalar **`Django`** usando Poetry

## Requerimientos previos

- Instalar **Pyenv**
- Instalar **Poetry**

## Instalar **`Django`**

Activar entorno virtual e instalar django usando poetry

```zsh
# Activamos entorno virtual
$> source venv/bin/activate

# Desactivamos entorno virtual
$> deactivate

# Instalar Django version 3.2.12 usando poetry
$> poetry add django@3.2.12

# Crear directorio src
$> mkdir -p src && cd src

# Configura proyecto Django con poetry
$> poetry run django-admin startproject server .
```

## Trabajando en el proyecto Django

```zsh
## Ejecutar servidor Django
$> poetry run python manage.py runserver 9898
```

## Bibliografía

- [Información sobre Django](https://www.djangoproject.com/)
