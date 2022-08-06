# Documentar usando MKDocs

MkDocs es un generador de sitios estáticos **rápido**, **simple** y **francamente magnífico** que está orientado a la creación de documentación de proyectos. Los archivos de origen de la documentación se escriben en Markdown y se configuran con un solo archivo de configuración YAML. Está diseñado para ser fácil de usar y se puede ampliar con temas, complementos y extensiones de Markdown de terceros.

## Características

- Cree archivos HTML estáticos a partir de archivos Markdown.
- Use complementos y extensiones Markdown para mejorar MkDocs.
- Use los temas integrados, temas de terceros o cree los suyos propios.
- Publique su documentación en cualquier lugar donde se puedan servir archivos estáticos.
- ¡Mucho más!

## Estructura básica de la documentación

```zsh
docs
└── mkdocs
    ├── README.md
    ├── docker-compose.yml
    ├── docs
    │   ├── CNAME
    │   ├── about
    │   │   ├── contributing.md
    │   │   └── license.md
    │   ├── index.md
    │   └── product
    ├── license.md
    └── mkdocs.yml
```

## Descripción de los ficheros más importantes

> **mkdocs.yml**
>
> En este fichero es donde se configura el proyecto de documentar usando **mkdocs**.

```yml
# -- Project information --
site_name: 'API Ripio DeFi'
site_description: 'Documentación del proyecto API Ripio DeFi usando mkdocs'
site_author: 'Ripio Team'
site_url: 'https://app.ripio.com'


# -- Repository --
repo_name: 'ripio/rp-defi'
repo_url: 'https://git.in.ripio.com/ripio/rp-defi'


# -- Copyright --
copyright: Derechos de autor &copy; 2022 <a href="https://app.ripio.com">Equipo de Ripio</a>, Mantenido por el equipo de Ripio.


# -- Configuration --
docs_dir: 'docs'
site_dir: 'static/docs/'

theme:
  name: 'material'
  language: 'es'
  features:
    - tabs
    - instant
  palette:
    primary: 'deep purple'
    accent: 'deep purple'
  font:
    text: 'Roboto'
    code: 'Roboto Mono'
  logo: assets/images/logo.svg
  favicon: assets/images/favicon.ico

# -- Customization --
extra:
  search:
    language: 'es'
  version:
    provider: mike

# Extensions
markdown_extensions:
  - markdown.extensions.admonition
  - markdown.extensions.attr_list

# -- Google Analytics --
#google_analytics:
#  - 'UA-XXXXXXXX-X'
#  - 'auto'


# -- Navigations --
nav:
  - Introducción: 'index.md'
  - Acerca de:
    - Contribución: about/contributing.md
    - Licencia: about/license.md


# -- Plugins --
plugins:
  - search:
      min_search_length: 4
```

> **docker-compose.yml**
>
> Con este fichero de configuración, se puede desplegar de forma local la documentión generada por MkDocs y revisar en el siguiente [enlace](http://localhost:8010).
>
> **RECUERDE**: debe estar posicionado en el directorio raíz de `mkdocs` al ejecutar los comandos que se muestran a continuación:

```zsh
# Desplegar documentación Sphinx
$> docker-compose up -d --build

# Remover contenedor de Sphinx
$> docker-compose down -v

# Para ver los logs del contenedor para revisar posibles problemas
$> docker logs mkdocs-documentation -f
```

```yaml
version: "3.9"

# ========================= SERVICES =======================
services:
  # ======================= MKDOCS =========================
  mkdocs:
    image: squidfunk/mkdocs-material
    container_name: mkdocs-documentation
    restart: always
    ports:
      - "8010:8010"
    command: serve -a 0.0.0.0:8010
    volumes:
      - ./docs:/docs/docs
      - ./mkdocs.yml:/docs/mkdocs.yml
    networks:
      - docs-mkdocs-network
  # ======================= MKDOCS =========================

# ========================= NETWORKS =======================
networks:
  docs-mkdocs-network:
    driver: bridge
```

## Bibliografía

- [Web oficial](https://www.mkdocs.org/)
