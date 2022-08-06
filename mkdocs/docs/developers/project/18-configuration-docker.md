# Configurar Docker y Docker Compose

## Conceptos básicos

### ¿Qué es Dockerfile?

Un Dockerfile es **un documento de texto que contiene todos los comandos que un usuario podría llamar en la línea de comandos para ensamblar una imagen**. Los usuarios de docker build pueden crear una compilación automatizada que ejecuta varias instrucciones de la línea de comandos en sucesión.

### Usar composición de Docker

Docker Compose proporciona una forma de orquestar varios contenedores que funcionan juntos. Los ejemplos incluyen un servicio que procesa solicitudes y un sitio web front-end, o un servicio que usa una función de soporte como un caché de Redis. Si usa el modelo de microservicios para el desarrollo de su aplicación, puede usar Docker Compose para factorizar el código de la aplicación en varios servicios que se ejecutan de forma independiente y que se comunican mediante solicitudes web.

### docker-compose.yml

Es muy tentador simplemente cambiar este archivo para agregar nuevos servicios a los ya existentes una vez. Sin embargo, su directorio git se ensuciará y siempre tendrá que guardar sus cambios antes de extraer nuevas funciones del control remoto. Para superar esto, Docker Compose ofrece un archivo de anulación predeterminado (`docker-compose.override.yml`) que le permite especificar cambios personalizados y servicios completamente nuevos sin tener que tocar el `docker-compose.yml` predeterminado.

> **NOTAS**
>
> Debe usar el signo de dólar doble (`$$`) para decirle a `docker-compose` que no analice estas variables de entorno.

### docker-compose.override.yml

`docker-compose.override.yml` es el archivo de configuración donde puede anular la configuración existente de `docker-compose.yml` o incluso agregar servicios completamente nuevos.

De forma predeterminada, este archivo no existe y debe crearlo. Puede copiar el `docker-compose.override.yml-example` existente o crear uno nuevo.

#### ¿Cómo funciona docker-compose.override.yml?

Cuando ejecuta `docker-compose up`, busca un archivo llamado `docker-compose.yml` y lee todos los servicios, redes, volúmenes, etc. configurados para crear su pila Docker. Si además tiene un archivo llamado `docker-compose.override.yml`, este también se leerá y se usará como un archivo de anulación para complementar. Funciona en el siguiente orden:

1. Se utilizarán todas las definiciones de `docker-compose.yml`
2. Todas las definiciones que también están definidas en `docker-compose.override.yml` sobrescribirán automáticamente la configuración de `docker-compose.yml`
3. Todas las definiciones que solo están disponibles en `docker-compose.override.yml` se agregarán adicionalmente.

Para iniciar su pila de Docker Compose, no se requieren pasos adicionales ni argumentos de línea de comando. Si ambos archivos existen, se leerán automáticamente.

### .dockerignore

El archivo .dockerignore es la herramienta que puede ayudarlo a definir el contexto de compilación de Docker que realmente necesita. Con este archivo, puede especificar ignorar reglas y excepciones de estas reglas para archivos y carpetas, que no se incluirán en el contexto de compilación y, por lo tanto, no se empaquetarán en un archivo ni se cargarán en el servidor Docker.

## Empecemos

### Configuraciones

Adicionar en el fichero **hosts** la siguiente configuración

```zsh
127.0.0.1 defi-database
```

> **NOTA**
>
> Ubicación del fichero **hosts**
>
> - **MAC**: `/etc/private/hosts`
> - **WINDOWS**: `c:\Windows\System32\Drivers\etc\hosts` 
> - **LINUX**: `/etc/hosts`
>
> Es necesario tener permisos de administrador.

Primero vamos a crear el fichero `.dockerignore` con el siguiente contenido:

> **.dockerignore**

```zsh
# In .dockerignore
# Exclude everything:
#
*

# Now un-exclude:
#
!src/media
!src/server
!src/manage.py
!pyproject.toml
```

Ahora procedemos a crear la estructura donde van los fichero `Dockerfile`

> **Estructura de directorios**

```zsh
docker
└── django
    └── Dockerfile
```

Con este fichero es que vamos a construir la imagen para poder desplegar los contenedores.

> Django `Dockerfile`

```dockerfile
# ======================================= ARGUMENTOS GLOBALES ======================================
ARG AENVIRONMENT=production
# ======================================= ARGUMENTOS GLOBALES ======================================

# ======================================= INSTALAR DEPENDENCIAS DEL PROYECTO =======================
# == USAR PARA DESARROLLO Y PRUEBA =================================================================
FROM python:3.9.4 AS development-builder

# -- Copiar los requerimientos de poetry --
COPY ./pyproject.toml ./opt/pyproject.toml

# -- Configurar el PATH del sistema
ENV PATH=/opt/venv/bin:$PATH

# -- Actualizar pip e instalar dependencias con poetry --
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && cd /opt \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

WORKDIR /opt
# == USAR PARA DESARROLLO Y PRUEBA =================================================================
# == USAR PARA PRODUCCION Y PUESTA EN ESCENA =======================================================
FROM python:3.9.4 AS production-builder

# -- Copiar los requerimientos de poetry --
COPY ./pyproject.toml ./opt/pyproject.toml

# -- Configurar el PATH del sistema
ENV PATH=/opt/venv/bin:$PATH

# -- Actualizar pip e instalar dependencias con poetry --
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && cd /opt \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

WORKDIR /opt
# == USAR PARA PRODUCCION Y PUESTA EN ESCENA =======================================================
# ======================================= INSTALAR DEPENDENCIAS DEL PROYECTO =======================

# ======================================= ADICIONAR EL CODIGO DEL PROYECTO =========================
# == USAR PARA DESARROLLO Y PRUEBA =================================================================
FROM python:3.9.4-slim-buster AS development-code

# -- Descripciones de la imagen --
LABEL maintainer="Ripio Team - support@ripio.com" \
    description="Image to deploy applications with the Django Framework" \
    vendor="Ripio" \
    license=MIT \
    version=1.0.0

# -- Establecer argumentos
# -- Nombre del grupo y usuario para ejecutar nuestra aplicacion --
ARG AAPP_GROUP=django
ARG AAPP_USER=defiapi
ARG ADJANGO_SETTINGS_MODULE=server.settings
ARG ATZ=America/Argentina/Buenos_Aires

# -- Establecer variables de entorno
# -- PYTHONDONTWRITEBYTECODE: si se establece en una cadena no vacía, Python no intentará escribir archivos .pyc en la importación de módulos fuente --
# -- PYTHONUNBUFFERED: permite que los mensajes de registro se vuelquen inmediatamente a la transmisión en lugar de almacenarse en búfer --
# -- LANG: establece la codificación utf-8 para Python. En general C. es para computadora --
# -- Adicionar al PATH del sistema --
# -- Agregue su archivo de configuración aquí --
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/opt/venv/bin \
    DJANGO_SETTINGS_MODULE=$ADJANGO_SETTINGS_MODULE \
    PATH=/opt/venv/bin:$PATH \
    TZ=$ATZ

# -- Copie solo la instalación de las dependencias de la imagen builder de la primera etapa --
COPY --from=development-builder /opt/venv /opt/venv

# -- Establecer directorio de trabajo --
WORKDIR /usr/src/app

# -- Instalar dependencias del sistema operativo --
RUN apt-get clean && DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \
    musl-dev \
    curl \
    libffi-dev \
    libpq-dev \
    libxslt-dev \
    swig \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

# -- Crear grupo y usuario para ejectuar la aplicación --
RUN groupadd -r ${AAPP_GROUP} && useradd --no-log-init -r -g ${AAPP_GROUP} ${AAPP_USER} \
    && chown -R ${AAPP_USER}:${AAPP_GROUP} /usr/src/app

# -- Cambiar a un usuario no root --
USER ${AAPP_USER}:${AAPP_GROUP}
# == USAR PARA DESARROLLO Y PRUEBA =================================================================
# == USAR PARA PRODUCCION Y PUESTA EN ESCENA =======================================================
FROM python:3.9.4-slim-buster AS production-code

# -- Descripciones de la imagen --
LABEL maintainer="Ripio Team - support@ripio.com" \
    description="Image to deploy applications with the Django Framework" \
    vendor="Ripio" \
    license=MIT \
    version=1.0.0

# -- Establecer argumentos
# -- Nombre del grupo y usuario para ejecutar nuestra aplicacion --
ARG AAPP_GROUP=django
ARG AAPP_USER=defiapi
ARG ADJANGO_SETTINGS_MODULE=server.settings
ARG ATZ=America/Argentina/Buenos_Aires

# -- Establecer variables de entorno
# -- PYTHONDONTWRITEBYTECODE: si se establece en una cadena no vacía, Python no intentará escribir archivos .pyc en la importación de módulos fuente --
# -- PYTHONUNBUFFERED: permite que los mensajes de registro se vuelquen inmediatamente a la transmisión en lugar de almacenarse en búfer --
# -- LANG: establece la codificación utf-8 para Python. En general C. es para computadora --
# -- Adicionar al PATH del sistema --
# -- Agregue su archivo de configuración aquí --
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONPATH=/opt/venv/bin \
    DJANGO_SETTINGS_MODULE=$ADJANGO_SETTINGS_MODULE \
    DJANGO_ENV=production \
    PATH=/opt/venv/bin:$PATH \
    TZ=$ATZ

# -- Copia las dependencias del proyecto para production --
COPY --from=production-builder /opt/venv /opt/venv

# -- Establecer directorio de trabajo --
WORKDIR /usr/src/app

# -- Instalar dependencias del sistema operativo --
RUN apt-get clean && DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \
    musl-dev \
    libffi-dev \
    libpq-dev \
    libxslt-dev \
    swig \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

COPY ./src .

# -- Crear grupo y usuario para ejectuar la aplicación --
RUN groupadd -r ${AAPP_GROUP} && useradd --no-log-init -r -g ${AAPP_GROUP} ${AAPP_USER} \
    && chown -R ${AAPP_USER}:${AAPP_GROUP} /usr/src/app

# -- Cambiar a un usuario no root --
USER ${AAPP_USER}:${AAPP_GROUP}
# == USAR PARA PRODUCCION Y PUESTA EN ESCENA =======================================================
# ======================================= ADICIONAR EL CODIGO DEL PROYECTO =========================

# ======================================= IMAGE TERMINADA ==========================================
FROM ${AENVIRONMENT}-code
# ======================================= IMAGE TERMINADA ==========================================
```

La configuración siguiente es utilizada por producción (PRODUCTION) o puesta en escena (STAGING)

> **docker-compose.yml**

```yaml
version: "3.9"

# ========================= SERVICES =======================
services:
  # ======================= DEFI API =======================
  defi-api:
    image: ripio/defi-api-prod:1.0.0
    container_name: defi-api-production
    build:
      context: .
      dockerfile: ./docker/django/Dockerfile
    command: >
      sh -c "gunicorn -c /usr/src/app/server/gunicorn_conf.py server.wsgi:application"
    restart: always
    env_file:
      - ./src/config/.env
    links:
      - defi-database
    depends_on:
      defi-database:
        condition: service_healthy
    ports:
      - 9099:9099
    networks:
      - defi-network
  # ======================= DEFI API =======================
  # ======================= POSTGRESQL DB ==================
  defi-database:
    container_name: defi-database
    image: postgres:11-alpine
    restart: always
    env_file:
      - ./src/config/.env
    ports:
      - 5432:5432
    volumes:
      - defi-investment-database:/var/lib/postgresql/data
    networks:
      - defi-network
    healthcheck:
      # We use `$$` here because:
      # one `$` goes to shell,
      # one `$` goes to `docker-compose.yml` escaping
      test: pg_isready -U $$POSTGRES_USER -h defi-database -p 5432 -d $$POSTGRES_DB -q
      interval: 10s
      timeout: 5s
      retries: 5
  # ======================= POSTGRESQL DB ==================

# ========================= VOLUMES ========================
volumes:
  defi-investment-database: {}

# ========================= NETWORKS =======================
networks:
  # Network for your internals, use it by default
  defi-network:
    name: defi-network
    driver: bridge
```

La configuración siguiente es utilizada para desarollo (DEVELOPMENT) o prueba (TESTING)

> **docker-compose.override.yml**

```yaml
# This docker-compose file is required to bind ports in development,
# since binding ports in regular compose file will ruin scaling
# in production. Due to how `ports` directive is merged with two files.
#
# This file is ignored in production, but
# it is automatically picked up in development with:
#
#  $ docker-compose up

version: "3.9"

# ========================= SERVICES =======================
services:

  # ======================= DEFI API =======================
  defi-api:
    image: ripio/defi-api-dev:1.0.0
    container_name: defi-api-development
    build:
      context: .
      dockerfile: ./docker/django/Dockerfile
      args:
        - AENVIRONMENT=development
    # command: "python3 -m http.server 9099"
    command: >
      sh -c "
        python manage.py migrate &&
        python manage.py runserver 0.0.0.0:9099"
    ports:
      - 9099:9099
    volumes:
      - ./src:/usr/src/app/
      - /usr/src/app/config
    healthcheck:
      # We use `$$` here because:
      # one `$` goes to shell,
      # one `$` goes to `docker-compose.yml` escaping
      test: /usr/bin/test $$(/usr/bin/curl -LI http://localhost:9099/health/?format=json -o /dev/null -w '%{http_code}\n' -s) -eq 200 || exit 1
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 20s
  # ======================= DEFI API =======================
```

Las variables de entorno configuradas por el proyecto

> **src/conf/.env**

```zsh
# Security Warning! Do not commit this file to any VCS!
# This is a local file to speed up development process,
# so you don't have to change your environment variables.
#
# This is not applied to `.env.template`!
# Template files must be committed to the VCS, but must not contain
# any secret values.


# === General ===

DOMAIN_NAME=example.com
TLS_EMAIL=webmaster@example.com


# === Django ===
# Generate yours with:
# python3 -c 'from django.utils.crypto import get_random_string; print(get_random_string(50))'

DJANGO_SECRET_KEY=B|wxPS,:f-6F.zy370}^/?QGTy.5<gRUO.t8y!*v0QovU0>)Yq


# === Database ===

# These variables are special, since they are consumed
# by both django and postgres docker image.
# Cannot be renamed if you use postgres in docker.
# See: https://hub.docker.com/_/postgres

POSTGRES_DB=defi_investment
POSTGRES_USER=defi
POSTGRES_PASSWORD=defi

# Used only by django:
DATABASE_URL=postgres://defi:defi@defi-database:5432/defi_investment
```

### Compilando

#### Compilar imagen con docker

```zsh
# Para compilar imagen para produccion y puesta en escena
$> docker build -t ripio/defi-api-prod:1.0.0 -f docker/django/Dockerfile --no-cache . 

# Para compilar imagen para desarrollo y pruebas
$> docker build -t ripio/defi-api-dev:1.0.0 -f docker/django/Dockerfile --build-arg AENVIRONMENT=development --no-cache . 
```

#### Compilar imagen con docker-compose y crear contenedor

```zsh
# Para compilar imagen y desplegar contenedor
$> docker-compose up -d --build --remove-orphans
```

> **NOTAS**
>
> 1. Recordar que si trabaja localmente para desarrollar alguna nueva especificación para el proyecto es necesario renombrar el fichero **docker-compose.override.yml-example** para **docker-compose.override.yml** el cual le va a permitir configurar todo lo necesario para poder desarrollar.
> 2. Los comandos anteriores se ejecutan desde la raíz principal del proyecto.

### Consejos

- **Eliminar contenedor y volumenes**

```zsh
# Con el siguiente comando eliminas el contenedor y los volumenes asociados al contenedor
$> docker-compose down -v --remove-orphans 
```

- **Revisar los logs del contenedor**

```zsh
# CONTAINER ID   IMAGE                      STATUS              NAMES
# e548ec59f31b   ripio/defi-api-prod:1.0.0  About a minute ago  defi-api-production

# docker logs CONTAINER ID OR NAMES -f
$> docker logs defi-api-production -f
$> docker logs e548ec59f31b -f
```

> **NOTA**
>
> Con la opción **-f** se mantiene escuchando los logs del contenedor.
>
> Para dejar de ver los logs utilizar `Ctrl + C`

- **Eliminar imagenes que no se utilizan**

```zsh
# Para conocer las imagenes de docker que tenemos localmente descargadas o creadas
$> docker images

# Para eliminar las imagenes de docker que no se esta utilizando
$> docker image prune

# REPOSITORY           TAG       IMAGE ID
# ripio/defi-api-prod  1.0.0     fb629ad721c2

# docker rmi -f IMAGE ID
# Para eliminar una imagen
$> docker rmi -f fb629ad721c2
```

- **Probar la conexion al contenedor defi-database**

```zsh
# Probando la conexión al contenedor postgresql 
$> docker exec -it defi-database psql postgres://usuario:contraseña@servidor:puerto/nombre_de_la_base_de_datos

# Probando la conexión al contenedor desde defi-api-development
$> docker exec -it defi-api-development ipython

In [1]: import psycopg2

# Establecer la conexión
In [2]: conn = psycopg2.connect(
   database="nombre_de_la_base_de_datos", user='usuario', password='contraseña', host='servidor', port= 'puerto'
)

# Crear un objeto cursor usando el método cursor()
In [3]: cursor = conn.cursor()

# Obtener la versión
In [4]: cursor.execute("select version()")

# Obtener una simple fila con el método fetchone().
In [5]: data = cursor.fetchone()

# Imprimir resultado
In [6]: print("Connection established to: ", data)

# SALIDA DE LA IMPRESION
Connection established to:  ('PostgreSQL 11.12 on x86_64-pc-linux-musl, compiled by gcc (Alpine 10.2.1_pre1) 10.2.1 20201203, 64-bit',)

# Cerrar la conexión
In [7]: conn.close()

# Salir de la shell del contenedor
In [8]: exit
```

- **Obtener configuración de la base de datos en `defi-api-development`**

```zsh
# Obtener configuraciñon de la base de datos del contenedor defi-api-development
$> docker exec -it defi-api-development ipython

In [1]: from django.conf import settings
In [2]: print(settings.DATABASES)
```

- **Verificar la salud del contenedor**

```zsh
$> docker inspect --format='{{json .State.Health}}' nombre_del_contenedor
```

## Bibliografía

- [Uso de ARG y ENV](https://vsupalov.com/docker-arg-env-variable-guide/)
- [Postgresq con docker](https://devops.datenkollektiv.de/using-a-postgresql-with-docker-like-a-pro.html)
- [Conexión segura con postgresql](https://itnext.io/postgresql-docker-image-with-ssl-certificate-signed-by-a-custom-certificate-authority-ca-3df41b5b53)
- [Watchman](https://adamj.eu/tech/2021/01/20/efficient-reloading-in-djangos-runserver-with-watchman/)
- [Pip-Tools](https://www.caktusgroup.com/blog/2018/09/18/python-dependency-management-pip-tools/)
- [Adicionar Healthcheck](https://howchoo.com/devops/how-to-add-a-health-check-to-your-docker-container)
