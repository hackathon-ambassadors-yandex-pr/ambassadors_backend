from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.content.views import ContentViewSet

router_contents_v1 = DefaultRouter()

router_contents_v1.register("", ContentViewSet, basename="contents")

urlpatterns = [
    path("", include(router_contents_v1.urls)),
]
