import logging

from ....libs.shared.serializers import KeySerializer
from ....libs.shared.services.http_client_service import HttpClientService
from ....libs.shared.constants import (APIS_HOST_ROUTES, X_API_KEY,)
from ....libs.shared.exceptions import ServiceNetworkException


# Configure Logger
LOGGER = logging.getLogger(__name__)


class UserService():
    """Manage user requests made to Prometeo API
    """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "X-API-Key": X_API_KEY,
    }

    @classmethod
    def me(cls, key):
        """Allows to obtain the information of the logged in user

        Args:
            key (string): Authentication key that should be used to obtain information from Prometeo API

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('USER_INFORMATION')}/"
        try:
            payload = KeySerializer(data={"key": key})
            payload.is_valid(raise_exception=True)
            response = HttpClientService.make_request(url=url, headers=cls.headers, verify=True, params=payload.data)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False


    @classmethod
    def account(cls, key):
        """Allows to obtain the account of the logged in user

        Args:
            key (string): Authentication key that should be used to obtain information from Prometeo API

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('USER_ACCOUNT')}/"
        try:
            payload = KeySerializer(data={"key": key})
            payload.is_valid(raise_exception=True)
            response = HttpClientService.make_request(url=url, headers=cls.headers, verify=True, params=payload.data)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False

    
    @classmethod
    def credit_cards(cls, key):
        """Allows to obtain the credit cards of the logged in user

        Args:
            key (string): Authentication key that should be used to obtain information from Prometeo API

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('USER_CREDIT_CARD')}/"
        try:
            payload = KeySerializer(data={"key": key})
            payload.is_valid(raise_exception=True)
            response = HttpClientService.make_request(url=url, headers=cls.headers, verify=True, params=payload.data)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False

