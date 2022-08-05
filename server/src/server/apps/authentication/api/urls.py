from rest_framework.routers import DefaultRouter

from .viewsets import (
    AuthenticationViewSet,
)

app_name = "authentication"

router = DefaultRouter(trailing_slash=False)
router.register(r"authentication", AuthenticationViewSet, basename="v1-authentication")

urlpatterns = router.urls
