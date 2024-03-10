"""Настройки URL эндпоинтов Sendings API v1."""

from apps.api.v1.sendings.views import SendingViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_sendings_v1 = DefaultRouter()

router_sendings_v1.register("", SendingViewSet, basename="sendings")

urlpatterns = [
    path("", include(router_sendings_v1.urls)),
]
