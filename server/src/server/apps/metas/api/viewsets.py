from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
)
from rest_framework import response
from rest_framework.views import APIView

from .serializers import ProviderResponseSerializer

from .services import MetasService


@extend_schema(tags=["V1 | Metas"])
class ProviderAPIView(APIView):
    
    @extend_schema(
        summary="List of providers",
        description="List all available data providers in Prometheus",
        parameters=[
            OpenApiParameter(
                name="key",
                description="For match with investment",
                required=True,
            ),
        ],
        examples=[
            OpenApiExample(
                name="Providers response successful",
                value={
                    "status": "success",
                    "key": [
                        {
                            "code": "bogota_corp_co",
                            "name": "Empresas - Banco de Bogota",
                            "country": "CO"
                        },
                        {
                            "code": "brou_pers_uy",
                            "name": "BROU",
                            "country": "UY"
                        }
                    ],
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
        request=None,
        responses={
            200: ProviderResponseSerializer
        },
    )
    def get(self, request):
        result = MetasService.provider(request.query_params.get('key'))
        response_serializer = ProviderResponseSerializer(data=result.json())
        response_serializer.is_valid(raise_exception=True)
        return response.Response(data=response_serializer.data)
