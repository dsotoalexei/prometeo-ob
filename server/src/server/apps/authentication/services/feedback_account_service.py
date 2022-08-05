import logging
from django.conf import settings
from rest_framework import status

from .serializers import WebhookAccountSerializer
from ....libs.shared.services.http_client_service import HttpClientService
from ....libs.shared.constants import (WEBHOOKS_PROVIDER_ROUTES,)
from ....libs.shared.exceptions import ServiceNetworkException


# Configure Logger
LOGGER = logging.getLogger(__name__)


class FeedbackAccountService():
    """Manage requests made to Ripio Webhooks
    """
    event_name = "feedback_account_event"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-WEBHOOKS-EVENT": event_name,
        # "Authorization": "Token {api_key}".format(api_key=settings.RIPIO_APIKEY)
    }

    @classmethod
    def validate_account(cls, account):
        """Allow to validate the account information

        Args:
            account (int): The account identifier

        Returns:
            Response: A dict representation of the APi'S JSON reply
            bool: Returns a false boolean if there is any error when making the request
        """
        url = f"{WEBHOOKS_PROVIDER_ROUTES.get('WEBHOOKS')}/"
        payload = WebhookAccountSerializer(data={"account": account})
        payload.is_valid(raise_exception=True)
        try:
            response = HttpClientService.make_request(url=url, method="post", headers=cls.headers, data=payload.data)
            if response.status_code == status.HTTP_200_OK:
                return response
            else:
                LOGGER.info(f"The Ripio Webhook failed")
        except ServiceNetworkException:
            LOGGER.exception(f"The remote server {url} returned an error")

        return False
