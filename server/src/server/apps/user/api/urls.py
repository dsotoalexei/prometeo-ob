from django.urls import path

from .viewsets import (
    UserMeAPIView,
    UserAccountAPIView,
    UserCreditCardsAPIView,
)

app_name = "user"

urlpatterns = [
    path('user/me/', UserMeAPIView.as_view(), name='me'),
    path('user/accounts/', UserAccountAPIView.as_view(), name='accounts'),
    path('user/credit-cards/', UserCreditCardsAPIView.as_view(), name='credit-cards'),
]
