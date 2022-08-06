# Instalar **`poetry`** en Pyenv usando entorno virtual

## Requerimientos previos

- Tener instalado **Pyenv**

## Configurar **`Poetry`**

Activar entorno virtual e instalar poetry

```zsh
# Activamos entorno virtual
$> source venv/bin/activate

# Desactivamos entorno virtual
$> deactivate

# Actualizar pip dentro del entorno virtual
$> pip install --upgrade pip

# Instalar poetry
$> pip install poetry
```

## Inicializar **`Poetry`**

```zsh
# Comando para generar configuraciones de Poetry
$> poetry init --no-interaction
```

Al ejecutar el comando anterior se genera el fichero `pyproject.toml`

Poetry utiliza el fichero `pyproject.toml` para específicar la configuración para sus proyectos. La configuración luce como se muestra a continuación:

```toml
[tool.poetry]
name = "rp-defi"
version = "0.1.0"
description = ""
authors = ["Ripio Team"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

### Descripción del fichero

Puede encontrar información sobre el fichero `pyproject.toml` en el siguiente [enlace](https://python-poetry.org/docs/master/pyproject/): https://python-poetry.org/docs/master/pyproject/

### Formas de instalar con Poetry

Al instalar con poetry usted puede especificar el paquete a instalar de la siguiente forma:

- Un simple nombre (requests)
- Un nombre y una restricción (requests@^2.23.0)
- Una url de git (git+https://github.com/python-poetry/poetry.git)
- Una url de git con una revisión (git+https://github.com/python-poetry/poetry.git#develop)
- El camino al fichero wheel (../my-package/my-package.whl)
- Un directorio (../my-package/)
- Una url (https://example.com/packages/my-package-0.1.0.tar.gz)

**Ejemplos**

```zsh
# Instalar un paquete
$> poetry add requests

# Instalar un paquete para desarrollo o prueba
$> poetry add -D pytest

# Desinstalar un paquete
$> poetry remove django
```

## Exportar dependencias en el fichero requirements.txt

Si necesita tener el archivo de `requirements.txt` con todas las dependencias, puede ejecutar la exportación de `poetry export -f requirements.txt --output requirements.txt`. Si configuró un trabajo de CI/CD que implementa automáticamente su proyecto, puede agregar esta función como un paso, lo que generará la versión actualizada en cada actualización.


## Instalar con poetry

El comando install lee el fichero pyproject.toml del proyecto actual, resuelve las dependencias y las instala.

```bash
$(venv) poetry install
```

Si hay un fichero `poetry.lock` en el directorio actual, utilizara las versiones exactas en vez de resolverlas. Esto asegura que todos usan la librería con la mismas dependencias.

Si no hay ningun fichero `poetry.lock`, Poetry creara uno después de resolver las dependencias.

Usted puede especificar al comando que no quiere las dependencias de desarrollo al pasar la opcion `--no-dev`.

```bash
$(venv) poetry install --no-dev
```

Si usted desea remover viejas dependencias no presentes en el fichero lock, use la opcion `--remove-untracked`.

```bash
$(venv) poetry install --remove-untracked
```

Usted también puede especificar los extras pasando la opcion `-E | --extras`.

```bash
$(venv) poetry install --extras "mysql pgsql"
$(venv) poetry install -E mysql -E pgsql
```

Por defecto poetry instala los paquetes del proyecto cuando se ejecuta `install`

```bash
$(venv) poetry install
```

Instalando dependencias desde el fichero lock

No dependencies to install or update

  - Installing <your-package-name> (x.x.x)

Si ustede quiere saltar esta instalación, use la opcion `--no-root`.

```bash
$(venv) poetry install --no-root
```

**Opciones:**

- **`--no-dev`**: No instalar dependencias de desarrollo.
- **`--no-root`**: No instalar paquete raiz (su proyecto).
- **`--extras (-E)`**: Características a instalar (son permitidos multiples valores).

## Bibliografía

- [Información sobre Poetry](https://python-poetry.org/)
