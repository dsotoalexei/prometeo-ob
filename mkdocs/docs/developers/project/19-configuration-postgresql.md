# Configurar postgresql

## Instalar dependencias

```zsh
$> poetry add dj-database-url psycopg2-binary
```

| Nombre   | Descripción                                 |
| -------- | ------------------------------------------- |
| dj-database-url | Use las URL de la base de datos en su aplicación Django. |
| psycopg2-binary | psycopg2 - Adaptador de base de datos Python-PostgreSQL |

## Configurar DATABASES

Adicionar la siguiente configuración en el fichero `database.py` ubicado en `src/server/settings/components`

```python
from dj_database_url import parse as db_url
from server.settings.components import config

# =======================================================================
# -- Database -- #
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# =======================================================================

DATABASE_URL = config("DATABASE_URL", None)
if not DATABASE_URL:
    raise ValueError('You must have "DATABASE_URL" variable')

default_db_config = config('DATABASE_URL', default='sqlite:///:memory:', cast=db_url,)
default_db_config['CONN_MAX_AGE'] = 600

DATABASES: object = {
    'default': default_db_config,
}
# =======================================================================
```

## Probar conexión desde la shell (tenemos IPython para este ejemplo)

```zsh
# Activamos el entorno virtual
$> source venv/bin/activate

# Nos posicionamos en el directorio donde se encuentra el fichero manage.py
$> cd src

# Lanzamos la shell
$> python manage.py shell

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

## Bibliografía

- [Documentación del paquete](https://pypi.org/project/dj-database-url/)
- [Ejemplo de uso](https://codigofacilito.com/articulos/hack-deploy-django-heroku)
