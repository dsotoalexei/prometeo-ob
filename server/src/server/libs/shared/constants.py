from rest_framework import status

from server.settings.components import config

# =======================================================================
# HTTP CLIENT SERVICE
# =======================================================================

# Number of retries for http requests
HTTP_MAX_RETRIES = 3

# How many seconds should request wait for in case non-critical error has occurred
HTTP_BACKOFF_FACTOR = 4

# Statuses which should trigger automatic retry
HTTP_RETRIES_STATUS_FORCELIST = [
    status.HTTP_408_REQUEST_TIMEOUT,
    status.HTTP_429_TOO_MANY_REQUESTS,
    status.HTTP_500_INTERNAL_SERVER_ERROR,
    status.HTTP_502_BAD_GATEWAY,
    status.HTTP_503_SERVICE_UNAVAILABLE,
    status.HTTP_504_GATEWAY_TIMEOUT
]

# HTTP methods that we should retry on
HTTP_RETRIES_METHODS_WHITELIST = ["HEAD", "GET", "OPTIONS"]

# Requests timeout in seconds
HTTP_REQUEST_TIMEOUT = 300

# HTTP methods allowed
HTTP_METHODS_ALLOWED = ['get', 'post', 'put', 'delete', 'patch']

# =======================================================================
# HTTP CLIENT SERVICE
# =======================================================================

# ======================================================================= 
# PROMETEO APIs
# =======================================================================

# Prometeo server Fully Qualified Domain Name (FQDN)
APIS_HOST = config("PROMETEO_BASE_URL")
X_API_KEY = config("PROMETEO_API_KEY")

# Separator for routes
SEP = '/'

# Routes to consult the Prometeo
APIS_HOST_ROUTES = {
    # HTTP METHOD [POST]
    'authentication_login': SEP.join([APIS_HOST, 'login']),
    'authentication_logout': SEP.join([APIS_HOST, 'logout'])
}

# =======================================================================
# PROMETEO APIs
# =======================================================================
