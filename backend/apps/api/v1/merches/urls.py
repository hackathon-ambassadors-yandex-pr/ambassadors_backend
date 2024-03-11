"""Настройки URL эндпоинтов Merches API v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.merches.views import MerchCreateListPartialUpdateViewSet

router_merches_v1 = DefaultRouter()

router_merches_v1.register("", MerchCreateListPartialUpdateViewSet, basename="merches")

urlpatterns = [
    path("", include(router_merches_v1.urls)),
]
