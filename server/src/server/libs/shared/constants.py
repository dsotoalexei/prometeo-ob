from rest_framework import status

# =======================================================================
# BEGIN CONSTANTS FOR HTTP CLIENT SERVICE
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
# END CONSTANTS FOR HTTP CLIENT SERVICE
# =======================================================================

# ======================================================================= 
# BEGIN CONSTANTS FOR TRADER SERVICE
# =======================================================================

# Webhooks server Fully Qualified Domain Name (FQDN)
WEBHOOKS_HOST = 'http://localhost:8000'

# Separator for routes
SEP = '/'

# Routes to consult the trader
WEBHOOKS_PROVIDER_ROUTES = {
    # HTTP METHOD [POST]
    'WEBHOOKS': SEP.join([WEBHOOKS_HOST, 'api', 'v3', 'webhooks'])
}

# Types of events allowed by the webhooks
EVENTS_ALLOWED = [
    'feedback_account_event',
    'feedback_transaction_event',
]


# =======================================================================
# END CONSTANTS FOR TRADER SERVICE
# =======================================================================
