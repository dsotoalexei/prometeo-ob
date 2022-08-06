# Instalar **`pyenv`** en macOS para Zsh usando Homebrew

## Requerimientos previos

- Instalar **Homebrew** y para eso puede ayudarse del siguiente [enlace](https://brew.sh/): https://brew.sh/
- Instalar **Zsh** mediante el siguiente [enlace](https://ohmyz.sh/): https://ohmyz.sh/

## Instalación

Instalar **`pyenv`** y **`pyenv-virtualenv`** mediante Homebrew

```zsh
# Actualizar brew
$> brew update

# Instalar pyenv
$> brew install pyenv

# Instalar pyenv-virtualenv
$> brew install pyenv-virtualenv
```

Adicionar las siguientes lineas al final del fichero **`.zshrc`** en su directorio raíz **`~`**

```zsh
### -- PYENV -- ###
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PIPENV_PYTHON="$PYENV_ROOT/shims/python"

plugin=(
    pyenv
)

eval "$(pyenv virtualenv-init -)"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
### -- PYENV -- ###
```

Recargar el fichero **`.zshrc`** para aplicar los cambios realizados

```zsh
# Recargar cambios
$> source ~/.zshrc
```

## Configurar Python **`3.9.4`**

```zsh
# Instalar python versión 3.9.4
$> pyenv install 3.9.4
```

## Definir raíz del proyecto

```zsh
# Creando el directorio
$> mkdir -p rp-defi && cd rp-defi

# Definir la version de python 3.9.4 dentro del directorio
$> pyenv local 3.9.4
```

## Crear el entorno virtual

- Usando `venv`

```zsh
# Crear entorno virtual
$> python -m venv venv

# Activamos entorno virtual
$> source venv/bin/activate

# Desactivamos entorno virtual
$> deactivate
```

- Usando `pyenv-virtualenv`

```zsh
# Crear entorno virtual
$> pyenv virtualenv 3.9.4 venv

# Activar entorno
$> pyenv activate venv

# Descativar entorno
$> pyenv deactivate

# Verificar los entornos virtuales
$> pyenv virtualenvs
```

## Bibliografía

- [Comandos de Pipenv](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)
- [Información de Pipenv](https://pipenv.pypa.io/en/latest/)
- [Mejores plugins para Zsh](https://travis.media/top-10-oh-my-zsh-plugins-for-productive-developers/)
