import logging
from django.conf import settings
from rest_framework import status

from .serializers import LoginRequestSerializer
from ....libs.shared.serializers import KeySerializer
from ....libs.shared.services.http_client_service import HttpClientService
from ....libs.shared.constants import (APIS_HOST_ROUTES, X_API_KEY,)
from ....libs.shared.exceptions import ServiceNetworkException


# Configure Logger
LOGGER = logging.getLogger(__name__)


class AuthenticationService():
    """Manage authentication requests made to Prometeo API
    """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "X-API-Key": X_API_KEY,
    }

    @classmethod
    def login(cls, data):
        """Login in Prometeo

        Args:
            data (string): The account identifier

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('authentication_login')}/"
        login_headers = cls.headers
        login_headers["Content-Type"] = "application/x-www-form-urlencoded"
        payload = LoginRequestSerializer(data=data)
        payload.is_valid(raise_exception=True)
        try:
            response = HttpClientService.make_request(url=url, method="post", headers=login_headers, data=payload.data, verify=True)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False

    @classmethod
    def logout(cls, key):
        """Logout in Prometeo

        Args:
            key (string): The account identifier

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('authentication_logout')}/"
        try:
            payload = KeySerializer(data={"key": key})
            payload.is_valid(raise_exception=True)
            response = HttpClientService.make_request(url=url, headers=cls.headers, verify=True, params=payload.data)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False
