from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
)
from rest_framework import response, status, viewsets
from rest_framework.views import APIView

from .serializers import (
    LoginRequestSerializer,
)

from ....libs.shared.serializers import PrometeoResponseSerializer

from .services import AuthenticationService


@extend_schema(tags=["V1 | Authentication"])
class LoginAPIView(APIView):
    
    @extend_schema(
        summary="Login",
        description="Log in",
        examples=[
            OpenApiExample(
                name="Login request example",
                value={
                    "provider": "test",
                    "username": "12345",
                    "password": "gfdsa",
                },
                request_only=True,  # signal that example only applies to requests
                response_only=False,  # signal that example only applies to responses
            ),
            OpenApiExample(
                name="Login response successful",
                value={
                    "status": "logged_in",
                    "key": "d303a064d60a4e73bd517d0002278c63",
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
        request=LoginRequestSerializer,
        responses={
            200: PrometeoResponseSerializer
        },
    )
    def post(self, request, *args, **kwargs):
        result = AuthenticationService.login(request.data)
        response_serializer = PrometeoResponseSerializer(data=result.json())
        response_serializer.is_valid(raise_exception=True)
        return response.Response(data=response_serializer.data)


@extend_schema(tags=["V1 | Authentication"])
class LogoutAPIView(APIView):
    
    @extend_schema(
        summary="Logout",
        description="Log out",
        parameters=[
            OpenApiParameter(
                name="key",
                description="For match with investment",
                required=True,
            ),
        ],
        examples=[
            OpenApiExample(
                name="Logout response successful",
                value={
                    "status": "logged_in",
                    "key": "d303a064d60a4e73bd517d0002278c63",
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
        request=None,
        responses={
            200: PrometeoResponseSerializer
        },
    )
    def get(self, request):
        result = AuthenticationService.logout(request.query_params.get('key'))
        response_serializer = PrometeoResponseSerializer(data=result.json())
        response_serializer.is_valid(raise_exception=True)
        return response.Response(data=response_serializer.data)
