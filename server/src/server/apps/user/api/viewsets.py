from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    extend_schema,
)
from rest_framework import response
from rest_framework.views import APIView

from .serializers import (
    InfoResponseSerializer,
    AccountResponseSerializer,
)

from .services import UserService


@extend_schema(tags=["V1 | User"])
class UserMeAPIView(APIView):
    
    @extend_schema(
        summary="User information",
        description="Allows to obtain the information of the logged in user",
        parameters=[
            OpenApiParameter(
                name="key",
                description="Authentication key that should be used to obtain information from Prometeo API",
                required=True,
            ),
        ],
        examples=[
            OpenApiExample(
                name="User information response successful",
                value={
                    "status": "success",
                    "info": {
                        "document": "12345",
                        "email": "test@example.com",
                        "name": "Test User"
                    }
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
        request=None,
        responses={
            200: InfoResponseSerializer
        },
    )
    def get(self, request):
        result = UserService.me(request.query_params.get('key'))
        response_serializer = InfoResponseSerializer(data=result.json())
        response_serializer.is_valid(raise_exception=True)
        return response.Response(data=response_serializer.data)


@extend_schema(tags=["V1 | User"])
class UserAccountAPIView(APIView):
    
    @extend_schema(
        summary="User accounts",
        description="Allows to obtain the accounts of the logged in user",
        parameters=[
            OpenApiParameter(
                name="key",
                description="Authentication key that should be used to obtain information from Prometeo API",
                required=True,
            ),
        ],
        examples=[
            OpenApiExample(
                name="User account response successful",
                value={
                    "status": "success",
                    "accounts": [
                        {
                            "id": "12345",
                            "name": "Test Account 1",
                            "number": "12345678",
                            "branch": "",
                            "currency": "UYU",
                            "balance": 21000
                        },
                        {
                            "id": "12346",
                            "name": "Test Account 2",
                            "number": "87654321",
                            "branch": "",
                            "currency": "USD",
                            "balance": 12000
                        }
                    ]
                },
                request_only=False,  # signal that example only applies to requests
                response_only=True,  # signal that example only applies to responses
            ),
        ],
        request=None,
        responses={
            200: AccountResponseSerializer
        },
    )
    def get(self, request):
        result = UserService.account(request.query_params.get('key'))
        response_serializer = AccountResponseSerializer(data=result.json())
        response_serializer.is_valid(raise_exception=True)
        return response.Response(data=response_serializer.data)
