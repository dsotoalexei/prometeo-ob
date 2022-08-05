from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
)

from .serializers import AuthSerializer

authentication_schema = dict(
    create=extend_schema(description="The list action returns all available currencies."),
)

