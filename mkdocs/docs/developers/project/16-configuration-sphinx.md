# Documentar el código con Sphinx

Sphinx es una herramienta que facilita la creación de documentación inteligente y hermosa, escrita por Georg Brandl y licenciada bajo la licencia BSD.

Originalmente fue creado para [la documentación de Python](https://docs.python.org/), y tiene excelentes instalaciones para la documentación de proyectos de software en una variedad de lenguajes. ¡Por supuesto, este sitio también se crea a partir de fuentes reStructuredText utilizando Sphinx! Cabe destacar las siguientes características:

- **Formatos de salida:** HTML (incluida la Ayuda HTML de Windows), LaTeX (para versiones PDF imprimibles), ePub, Texinfo, páginas de manual, texto sin formato
- **Extensas referencias cruzadas:** marcado semántico y enlaces automáticos para funciones, clases, citas, términos del glosario y piezas de información similares
- **Estructura jerárquica:** fácil definición de un árbol de documentos, con enlaces automáticos a hermanos, padres e hijos
- **Índices automáticos:** índice general así como índices de módulos específicos del idioma
- **Manejo de código:** resaltado automático usando el resaltador [Pygments](https://pygments.org/)
- **Extensiones:** pruebas automáticas de fragmentos de código, inclusión de cadenas de documentos de módulos de Python (documentos API) y [más](https://www.sphinx-doc.org/en/master/ext/builtins.html# extensiones-esfinge-incorporadas)
- **Extensiones aportadas:** docenas de extensiones [aportadas por usuarios](https://www.sphinx-doc.org/en/master/usage/extensions/index.html#third-party-extensions); la mayoría de ellos instalables desde PyPI

Sphinx usa [reStructuredText](https://docutils.sourceforge.io/rst.html) como su lenguaje de marcado, y muchas de sus fortalezas provienen del poder y la sencillez de reStructuredText y su paquete de análisis y traducción, el [Docutils]( https://docutils.sourceforge.io/).

## Instalar Sphinx

Instalar el paquete de Sphinx en modo desarrollo

```zsh
$> poetry add -D sphinx
```

Para poder generar la documentación a partir de los módulos del proyecto ejecutar el siguiente comando:

```zsh
$> sphinx-apidoc -f -o ./docs/sphinx/docs/source/ ./src/server/apps
```

## Estructura básica de la documentación

```zsh
docs
└── sphinx
    ├── Dockerfile
    ├── README.md
    ├── docker-compose.yml
    ├── docs
    │   ├── Makefile
    │   ├── build
    │   ├── make.bat
    │   └── source
    │       ├── readme.rst
    └── license.md
```

## Descripción de los ficheros más importantes

> **Dockerfile**
>
> Este fichero permite crear la imagen que va a desplegar la documentación de Sphinx en el puerto 9011 (El puerto se puede modificar)

```dockerfile
# =========================================== STAGE BUILDER ===========================================
FROM python:3.9 AS builder

# -- Establecer directorio de trabajo --
WORKDIR /opt

# -- Definir variable de entorno VIRTUAL_ENV=/opt/venv que es donde se instalarán las dependencias del proyecto
ENV VIRTUAL_ENV=/opt/venv

# -- Creando entorno virtual de python con el comando venv
RUN python3 -m venv $VIRTUAL_ENV

# -- Configurar la variable de entorno VIRTUAL_ENV en el camino del sistema
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# -- Actualizar pip e instalar dependencias --
RUN pip install --upgrade pip \
    && pip install sphinx sphinx-autobuild recommonmark sphinx_rtd_theme sphinxcontrib-swaggersphinx sphinxcontrib-jupyter sphinx-autodoc-napoleon-typehints sphinx-autodoc-typehints

# =========================================== STAGE BUILDER ===========================================

# =========================================== STAGE FINAL =============================================
FROM python:3.9-slim-buster

# -- Descripciones de la imagen --
LABEL maintainer="Alexei Díaz Soto - alexei.diaz@ripio.com" \
    description="Imagen para desplegar documentación de Sphinx" \
    vendor="Ripio Team" \
    license="MIT" \
    version="1.0.0"

# -- Establecer variables de entorno
# -- PYTHONDONTWRITEBYTECODE: si se establece en una cadena no vacía, Python no intentará escribir archivos .pyc en la importación de módulos fuente --
# -- PYTHONUNBUFFERED: permite que los mensajes de registro se vuelquen inmediatamente a la transmisión en lugar de almacenarse en búfer --
# -- LANG: establece la codificación utf-8 para Python. En general C. es para computadora --
ENV PYTHONDONTWRITEBYTECODE="1" \
    PYTHONUNBUFFERED="1" \
    LANG="C.UTF-8" \
    LC_ALL="C.UTF-8" \
    PATH="/opt/venv/bin:$PATH"

# -- Copie solo la instalación de las dependencias de la imagen builder de la primera etapa --
COPY --from=builder /opt/venv /opt/venv

# -- Establecer directorio de trabajo --
WORKDIR /usr/src/docs

EXPOSE 9011

CMD ["/bin/bash", "-c", "sphinx-autobuild -a /usr/src/docs/source /usr/src/docs/build/html --host 0.0.0.0 --port 9011  --watch /usr/src/docs/source" ]
# =========================================== STAGE FINAL =============================================
```

> **docker-compose.yml**
>
> Con este fichero de configuración, se puede desplegar de forma local la documentión generada por Sphinx.
>
> **RECUERDE**: debe estar posicionado en el directorio raíz de `sphinx` al ejecutar los comandos que se muestran a continuación:

```zsh
# Desplegar documentación Sphinx
$> docker-compose up -d --build

# Remover contenedor de Sphinx
$> docker-compose down -v

# Para ver los logs del contenedor para revisar posibles problemas
$> docker logs sphinx-documentation -f
```

```yaml
version: '3.9'

# ========================= SERVICES =======================
services:

  # ======================= SPHINX =========================
  sphinx:
    image: sphinx/sphinx-docs:1.0.0
    build:
      context: .
      dockerfile: ./Dockerfile
    container_name: sphinx-documentation
    restart: always
    ports:
      - '9011:9011'
    volumes:
      - ./docs:/usr/src/docs
    networks:
      - docs-sphinx-network
  # ======================= SPHINX =========================

# ========================= NETWORKS =======================
networks:
  docs-sphinx-network:
    driver: bridge
```

> **docs/source/readme.rst**
>
> Este es un ejemplo de un readme.rst (Se debe modificar para generar el propio readme del proyecto)

```rst
Sample Binary Tree Library
##########################

.. image:: https://github.com/shunsvineyard/python-sample-code/workflows/Test/badge.svg
    :target: https://github.com/shunsvineyard/python-sample-code/actions?query=workflow%3ATest

.. image:: https://github.com/shunsvineyard/python-sample-code/workflows/Linting/badge.svg
    :target: https://github.com/shunsvineyard/python-sample-code/actions?query=workflow%3ALinting

.. image:: https://codecov.io/gh/shunsvineyard/python-sample-code/branch/main/graph/badge.svg?token=zLkKU6p7do
    :target: https://codecov.io/gh/shunsvineyard/python-sample-code

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black


The **Binary Tree Library** is a Python sample project used by shunsvineyard.info. It is an example for `Sphinx <https://www.sphinx-doc.org/>`_ and `My Python Coding Style <https://shunsvineyard.info/2019/01/05/my-python-coding-style-and-principles/>`_.

Although it is a sample project, the **Binary Tree Library** is a usable tree data structure library, and has the following tree data structures:

- AVL Tree
- Binary Search Tree
- Red Black Tree
- Threaded Binary Trees

The library also provides the tree traversal feature to traverse binary trees.

- Binary Tree Traversal
    - In-order
    - Reversed In-order
    - Pre-order
    - Post-order
    - Level-order

Requirements
------------

The **Binary Tree Library** requires Python 3.7 or newer.
The key Python 3.7 feature used in the project is `dataclass <https://docs.python.org/3/library/dataclasses.html#module-dataclasses>`_.

Installation
------------

Install from Github

.. code-block:: text

    git clone https://github.com/shunsvineyard/python-sample-code.git
    cd python-sample-code
    pip install .

Examples
--------

.. code-block:: python

    from trees import tree_exceptions
    from trees.binary_trees import red_black_tree
    from trees.binary_trees import traversal


    class Map:
        def __init__(self):
            self._rbt = red_black_tree.RBTree()

        def __setitem__(self, key, value):
            self._rbt.insert(key=key, data=value)

        def __getitem__(self, key):
            return self._rbt.search(key=key).data

        def __delitem__(self, key):
            self._rbt.delete(key=key)

        def __iter__(self):
            return traversal.inorder_traverse(tree=self._rbt)


    if __name__ == "__main__":

        # Initialize the Map instance.
        contacts = Map()

        # Add some items.
        contacts["Mark"] = "mark@email.com"
        contacts["John"] = "john@email.com"
        contacts["Luke"] = "luke@email.com"
        contacts["john"] = "john@email.com"

        # Iterate the items.
        for contact in contacts:
            print(contact)

        # Delete one item.
        del contacts["john"]

        # Check the deleted item.
        try:
            print(contacts["john"])
        except tree_exceptions.KeyNotFoundError:
            print("john does not exist")


Tree CLI
--------

The **Binary Tree Library** provides a command line tool to simulate tree data structures.

.. code-block:: text

    tree-cli

It will show the interactive prompt. Use ``help`` to list all the available commands


.. code-block:: text

    Welcome to the Tree CLI. Type help or ? to list commands.

    tree> help

    Documented commands (type help <topic>):
    ========================================
    build  delete  destroy  detail  exit  help  insert  search  traverse
```

## Bibliografía

- [Web Oficial](https://www.sphinx-doc.org/en/master/)
- [Usar Sphinx](https://shunsvineyard.info/2019/09/19/use-sphinx-for-python-documentation/)
- [Ejemplo 1](https://betterprogramming.pub/auto-documenting-a-python-project-using-sphinx-8878f9ddc6e9)
