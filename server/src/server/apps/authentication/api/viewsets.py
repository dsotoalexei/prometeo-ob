from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import response, status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action

from .schemas import (
    authentication_schema,
)
from .serializers import (
    EmptyPayloadResponseSerializer,
    AuthSerializer
)


@extend_schema(tags=["V1 | Authentication"])
class EmptyPayloadAPI(APIView):
    
    @extend_schema(request=None, responses=EmptyPayloadResponseSerializer)
    def get(self, request, *args, **kwargs):
        # some actions
        return response.Response(data={"detail": "Success"})
