from django.urls import path

from .viewsets import (
    UserMeAPIView,
    UserAccountAPIView,
)

app_name = "user"

urlpatterns = [
    path('user/me/', UserMeAPIView.as_view(), name='me'),
    path('user/account/', UserAccountAPIView.as_view(), name='account'),
]
