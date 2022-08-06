import json
import logging
import sys

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from rest_framework.utils.serializer_helpers import ReturnDict
from ..exceptions import ServiceNetworkException
from ..constants import (
    HTTP_MAX_RETRIES,
    HTTP_METHODS_ALLOWED,
    HTTP_REQUEST_TIMEOUT,
    HTTP_RETRIES_STATUS_FORCELIST,
    HTTP_BACKOFF_FACTOR,
    HTTP_RETRIES_METHODS_WHITELIST
)


# Configure Logger
LOGGER = logging.getLogger(__name__)


class TimeoutHTTPAdapter(HTTPAdapter):
    """This class defines a custom Transport Adapter with default timeouts
    
    Using Transport Adapters we can set a default timeout for all HTTP calls.
    This ensures that a sensible timeout is set even if the developer forgets
    to add the timeout=1 parameter to his individual call, but allows for overrides on a per-call basis.
    """

    def __init__(self, *args, **kwargs):
        """Initialize the class.
        """
        self.timeout = HTTP_REQUEST_TIMEOUT
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super(TimeoutHTTPAdapter, self).__init__(*args, **kwargs)


class HttpClientService():
    """This class defines the wrapper for requests library.
    """
    retry_strategy = Retry(
        total=HTTP_MAX_RETRIES,
        connect=HTTP_MAX_RETRIES,
        backoff_factor=HTTP_BACKOFF_FACTOR,
        status_forcelist=HTTP_RETRIES_STATUS_FORCELIST,
        method_whitelist=HTTP_RETRIES_METHODS_WHITELIST
    )
    adapter = TimeoutHTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    @classmethod
    def make_request(cls, url, method='get', headers=None, data=None, verify=False, timeout=None, params=None):
        """Reusable method for performing requests

        Args:
            url (str): Url to request
            method (str): Request method, default is 'get'
            headers (dict): Request headers
            data (dict): Data to be sent
            verify (bool): Whether or not to verify SSL cert, default to False
            timeout (int): The timeout of the request in second, default to None
            params (dict): Additional query parameters for request

        Returns:
            Response: A dict representation of the APi'S JSON reply

        Raises:
            ServiceNetworkException: The remote server returned an error
            RuntimeError: Unsupported method for requests call!
        """
        method = method.lower()
        if method not in HTTP_METHODS_ALLOWED:
            raise RuntimeError("Unsupported method '%s' for requests call!" % method)

        request = getattr(cls.http, method)
        headers = headers or {}

        # if isinstance(data, ReturnDict):
        #     data = json.dumps(data)

        response = requests.Response()

        try:
            with request(url=url, headers=headers, data=data, verify=verify, timeout=timeout, params=params) as res:
                response = res
                response.raise_for_status()

                return response
        except requests.exceptions.HTTPError as ex:
            raise ServiceNetworkException(url, str(ex), '', cause=ex, traceback=sys.exc_info()[2]) from None
        except (requests.exceptions.RetryError, requests.exceptions.Timeout) as ex:
            raise ServiceNetworkException(url, str(ex), '', cause=ex, traceback=sys.exc_info()[2]) from None
        except requests.exceptions.ConnectionError as ex:
            raise ServiceNetworkException(url, str(ex), '', cause=ex, traceback=sys.exc_info()[2]) from None
    
    @classmethod
    def clear_cookies(cls):
        """Method for clear the cookies
        """
        cls.http.cookies.clear()

    def __str__(self):
        """Represents the class objects as a string

        Returns:
            str: Name that describes the class
        """
        return "Http Client Service"
