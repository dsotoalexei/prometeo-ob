from functools import wraps

from django.conf import settings
from django.utils.encoding import smart_text

import jwt
from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response


def check_rsa(view_func):
    """_summary_

    Args:
        function (_type_): _description_
    """

    def wrapper1(*args, **kwargs):
        """_summary_"""
        auth_header_prefix = "credit_bearer"
        auth = get_authorization_header(args[1]).split()
        if smart_text(auth[0].lower()) != auth_header_prefix:
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        jwt_value = auth[1]
        key = settings.CREDIT_PUBLIC_KEY
        try:
            payload = jwt.decode(
                jwt_value,
                key,
                "RS256",
            )
        except jwt.DecodeError:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        if str(payload.get("api-key", None)) != settings.API_KEY_CREDIT:
            return Response({}, status=status.HTTP_403_FORBIDDEN)
        return view_func(*args, **kwargs)

    return wrapper1


def check_account(countries):
    """Decorator that verifies that the account is operational and within the allowed countries

    Args:
        countries list(str): Country Alpha-2 code to which the operation is allowed
    """

    def wrapper(view_func):
        """_summary_"""

        @wraps(view_func)
        def _wrapper(self, *args, **kwargs):
            """_summary_"""
            if not self.request.account.is_fully_operative():
                return Response(
                    {"detail": "Account is not fully operative"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            if self.request.account.country not in countries:
                return Response(
                    {"detail": "Account is not country available"},
                    status=status.HTTP_403_FORBIDDEN,
                )
            return view_func(self, *args, **kwargs)

        return _wrapper

    return wrapper
