"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from health_check import urls as health_urls

from server.apps.authentication.api import urls as authentication_urls
from server.apps.metas.api import urls as metas_urls
from server.apps.user.api import urls as user_urls

api_v1_urlpatterns = [
    path("api/v1/", include(authentication_urls, namespace="v1-authentication")),
    path("api/v1/", include(metas_urls, namespace="v1-metas")),
    path("api/v1/", include(user_urls, namespace="v1-user")),
]

urlpatterns = [
    # path("admin/", admin.site.urls),
    # API Documentation
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/v1/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    # Health checks:
    path("health/", include(health_urls)),
] 

# enable serve static by django for local development
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# API VERSION 1
urlpatterns += api_v1_urlpatterns
