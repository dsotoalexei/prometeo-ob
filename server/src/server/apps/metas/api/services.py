import logging

from ....libs.shared.serializers import KeySerializer
from ....libs.shared.services.http_client_service import HttpClientService
from ....libs.shared.constants import (APIS_HOST_ROUTES, X_API_KEY,)
from ....libs.shared.exceptions import ServiceNetworkException


# Configure Logger
LOGGER = logging.getLogger(__name__)


class MetasService():
    """Manage metas requests made to Prometeo API
    """
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
        "X-API-Key": X_API_KEY,
    }

    @classmethod
    def provider(cls):
        """Get a list of providers from Prometeo API

        Args:
            key (string): The account identifier

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{APIS_HOST_ROUTES.get('METAS_PROVIDERS')}/"
        try:
            response = HttpClientService.make_request(url=url, headers=cls.headers, verify=True)
            return response
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False
