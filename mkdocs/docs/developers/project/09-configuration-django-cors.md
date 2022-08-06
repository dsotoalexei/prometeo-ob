# Adicionar CORS Header

## Instalar dependencias

```zsh
$> poetry add django-cors-headers
```

| Nombre              | Descripción                                                  |
| ------------------- | ------------------------------------------------------------ |
| django-cors-headers | Agrega encabezados de intercambio de recursos de origen cruzado (CORS) a las respuestas |

## Configurar CORS

> **NOTA**
>
> `CorsMiddleware` debe colocarse lo más alto posible, especialmente antes de cualquier middleware que pueda generar respuestas como **CommonMiddleware** de Django o **WhiteNoiseMiddleware** de Whitenoise. Si no es antes, no podrá agregar los encabezados **CORS** a estas respuestas.
>
> Además, si está utilizando **CORS_REPLACE_HTTPS_REFERER**, debe colocarse antes de **CsrfViewMiddleware** de Django

Crear fichero `cors.py` en la ubicación `src/server/settings/components/`

```python
from server.settings.components import config

# CORS HEADERS CONFIGURATION
# -- Allows any client access
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',
    'http://localhost:5000',
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
```

Adicionar configuración en el fichero `src/server/settings/__init__.py`

```python
base_settings = [
    ...
    'components/cors.py',
		...
]
```

Adicionar configuración en el fichero `src/server/settings/components/common.py`

```python
# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    ...
  	# CORS HEADERS
    'corsheaders',
)

MIDDLEWARE: Tuple[str, ...] = (
   # CORS HEADERS
   'corsheaders.middleware.CorsMiddleware',
   ...
)
```

## Información sobre otras configuraciones de CORS HEADERS

### Descripción de variables de configuración

#### `CORS_ALLOWED_ORIGINS`

Una lista de orígenes que están autorizados para realizar solicitudes HTTP entre sitios. El valor predeterminado es `[]`.

Un origen se define mediante [la sección 3.2 de CORS RFC](https://tools.ietf.org/html/rfc6454#section-3.2) como un esquema de URI + nombre de host + puerto, o uno de los valores especiales 'null' o 'expediente: //'. Los puertos predeterminados (HTTPS = 443, HTTP = 80) son opcionales aquí.

El navegador envía el valor especial nulo en ["contextos sensibles a la privacidad"](https://tools.ietf.org/html/rfc6454#section-6), como cuando el cliente se ejecuta desde un `archivo: //` dominio. Algunas versiones de Chrome en Android envían accidentalmente el archivo de valor especial: // según [este error](https://bugs.chromium.org/p/chromium/issues/detail?id=991107).

**Ejemplo**:

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]
```

Anteriormente, esta configuración se llamaba `CORS_ORIGIN_WHITELIST`, que todavía funciona como un alias, y el nuevo nombre tiene prioridad.

#### `CORS_ALLOWED_ORIGIN_REGEXES`

Una lista de cadenas que representan expresiones regulares que coinciden con los orígenes que están autorizados para realizar solicitudes HTTP entre sitios. El valor predeterminado es `[]`. Útil cuando `CORS_ALLOWED_ORIGINS` no es práctico, como cuando tiene una gran cantidad de subdominios.

**Ejemplo**:

```python
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.example\.com$",
]
```

Anteriormente, esta configuración se llamaba `CORS_ORIGIN_REGEX_WHITELIST`, que todavía funciona como un alias, con el nuevo nombre teniendo prioridad.

#### `CORS_ALLOW_ALL_ORIGINS`

Si es `true`, se permitirán todos los orígenes. Se ignorarán otras configuraciones que restrinjan los orígenes permitidos. El valor predeterminado es `false`.

**Establecer esto en `true` puede ser *peligroso***, ya que permite que cualquier sitio web realice solicitudes de origen cruzado al suyo. Generalmente querrá restringir la lista de orígenes permitidos con `CORS_ALLOWED_ORIGINS` o `CORS_ALLOWED_ORIGIN_REGEXES`.

Anteriormente, esta configuración se llamaba `CORS_ORIGIN_ALLOW_ALL`, que todavía funciona como un alias, con el nuevo nombre teniendo prioridad.

------

> **Las siguientes son configuraciones opcionales, para las cuales los valores predeterminados probablemente sean suficientes.**

#### `CORS_URLS_REGEX`

Una expresión regular que restringe las URL para las que se enviarán los encabezados CORS. El valor predeterminado es `r'^.*$'`, es decir, coincide con todas las URL. Útil cuando solo necesita CORS en una parte de su sitio, p. una API en `/api/`.

**Ejemplo**:

```python
CORS_URLS_REGEX = r'^/api/.*$'
```

#### `CORS_ALLOW_METHODS`

Una lista de verbos HTTP que están permitidos para la solicitud real. Predeterminado a:

```python
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
```

El valor predeterminado se puede importar como `corsheaders.defaults.default_methods` para que pueda ampliarlo con sus métodos personalizados. Esto le permite mantenerse al día con cualquier cambio futuro. Por ejemplo:

```python
from corsheaders.defaults import default_methods

CORS_ALLOW_METHODS = list(default_methods) + [
    'POKE',
]
```

#### `CORS_ALLOW_HEADERS`

La lista de encabezados HTTP no estándar que se pueden usar al realizar la solicitud real. Predeterminado a:

```python
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

El valor predeterminado se puede importar como `corsheaders.defaults.default_headers` para que pueda ampliarlo con sus encabezados personalizados. Esto le permite mantenerse al día con cualquier cambio futuro. Por ejemplo:

```python
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = list(default_headers) + [
    'my-custom-header',
]
```

#### `CORS_EXPOSE_HEADERS`

La lista de encabezados HTTP que se van a exponer al navegador. El valor predeterminado es `[]`.

#### `CORS_PREFLIGHT_MAX_AGE`

La cantidad de segundos que un cliente/navegador puede almacenar en caché la respuesta de verificación previa. Si es 0 (o cualquier valor falso), no se enviará ningún encabezado de edad máxima. El valor predeterminado es `86400` (un día).

> **NOTA**
>
> Una solicitud de verificación previa (preflight) es una solicitud adicional que se realiza cuando se realiza una solicitud "no tan simple" (por ejemplo, `Content-Type` no es `application/x-www-form-urlencoded`) para determinar qué solicitudes acepta realmente el servidor . Obtenga más información al respecto en el [artículo de CORS MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Preflighted_requests).

#### `CORS_ALLOW_CREDENTIALS`

Si es `true`, se permitirá incluir cookies en solicitudes HTTP entre sitios. El valor predeterminado es `Falso`.

> **NOTA**
>
> En Django 2.1 se agregó la configuración [SESSION_COOKIE_SAMESITE](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SESSION_COOKIE_SAMESITE), configurada en `'Lax'` por defecto, lo que evitará que la cookie de sesión de Django se envíe entre dominios. Cámbielo a `None` para eludir esta restricción de seguridad.

### Integración CSRF

La mayoría de los sitios deberán aprovechar la [Protección contra la falsificación de solicitudes entre sitios](https://docs.djangoproject.com/en/3.0/ref/csrf/) que ofrece Django. CORS y CSRF están separados, y Django no tiene forma de usar su configuración de CORS para eximir a los sitios de la verificación de `Referer` que hace en solicitudes seguras. La forma de hacerlo es con su [configuración CSRF_TRUSTED_ORIGINS](https://docs.djangoproject.com/en/3.0/ref/settings/#csrf-trusted-origins).

**Por ejemplo**:

```python
CORS_ALLOWED_ORIGINS = [
    'http://read.only.com',
    'http://change.allowed.com',
]

CSRF_TRUSTED_ORIGINS = [
    'change.allowed.com',
]
```

#### `CORS_REPLACE_HTTPS_REFERER`

`CSRF_TRUSTED_ORIGINS` se introdujo en Django 1.9, por lo que los usuarios de versiones anteriores necesitarán una solución alternativa. Si `CORS_REPLACE_HTTPS_REFERER` es `True`, `CorsMiddleware` cambiará el encabezado `Referer` a algo que pasará las comprobaciones CSRF de Django cada vez que pasen las comprobaciones CORS. El valor predeterminado es `Falso`.

Tenga en cuenta que, a diferencia de `CSRF_TRUSTED_ORIGINS`, esta configuración no le permite distinguir entre dominios en los que CORS confía para *leer* recursos y dominios en los que confía *cambiar* recursos al evitar la protección CSRF.

Con esta función habilitada, también debe agregar `corsheaders.middleware.CorsPostCsrfMiddleware` después de `django.middleware.csrf.CsrfViewMiddleware` en su `MIDDLEWARE_CLASSES` para deshacer el reemplazo `Referer`:

```python
MIDDLEWARE_CLASSES = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    ...
]
```

### Señales (Signals)

Si tiene un caso de uso que requiere más que solo la configuración anterior, puede adjuntar un código para verificar si se debe permitir una solicitud determinada. Por ejemplo, esto se puede usar para leer la lista de orígenes que permite de un modelo. Adjunte cualquier cantidad de controladores a `check_request_enabled` [señal de Django](https://docs.djangoproject.com/en/3.0/ref/signals/), que proporciona el argumento `request` (use `**kwargs` en su controlador para protegerse contra cualquier argumento futuro que se agregue). Si algún controlador adjunto a la señal devuelve un valor verdadero, se permitirá la solicitud.

Por ejemplo, podría definir un controlador como este:

```python
# myapp/handlers.py
from corsheaders.signals import check_request_enabled

from myapp.models import MySite

def cors_allow_mysites(sender, request, **kwargs):
    return MySite.objects.filter(host=request.host).exists()

check_request_enabled.connect(cors_allow_mysites)
```

Luego, conéctelo cuando la aplicación esté lista usando [Django AppConfig](https://docs.djangoproject.com/en/3.0/ref/applications/):

```python
# myapp/__init__.py

default_app_config = 'myapp.apps.MyAppConfig'
# myapp/apps.py

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Makes sure all signal handlers are connected
        from myapp import handlers  # noqa
```

Un caso de uso común para la señal es permitir que *todos* los orígenes accedan a un subconjunto de URL, mientras que permite que un conjunto normal de orígenes acceda a *todas* las URL. Esto no es posible usando solo la configuración normal, pero se puede lograr con un controlador de señal.

Primero configure `CORS_ALLOWED_ORIGINS` en la lista de orígenes confiables que pueden acceder a cada URL y luego agregue un controlador a `check_request_enabled` para permitir CORS independientemente del origen de las URL sin restricciones.

**Por ejemplo:**

```python
# myapp/handlers.py
from corsheaders.signals import check_request_enabled

def cors_allow_api_to_everyone(sender, request, **kwargs):
    return request.path.startswith('/api/')

check_request_enabled.connect(cors_allow_api_to_everyone)
```

## Bibliografía

- [Como arregla el error CORS en Django](https://dzone.com/articles/how-to-fix-django-cors-error)
- [Información del paquete](https://pypi.org/project/django-cors-headers/)
- [Guía sobre Cors](https://www.stackhawk.com/blog/django-cors-guide/)
