from django.urls import path

from .viewsets import (
    LoginAPIView,
    LogoutAPIView,
)

app_name = "authentication"

urlpatterns = [
    path('authentication/login/', LoginAPIView.as_view(), name='login'),
    path('authentication/logout/', LogoutAPIView.as_view(), name='logout'),
]
