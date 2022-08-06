from django.urls import path

from .viewsets import (
    ProviderAPIView,
)

app_name = "metas"

urlpatterns = [
    path('metas/provider/', ProviderAPIView.as_view(), name='provider'),
]
