from apps.api.v1.content.views import ContentViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_sendings_v1 = DefaultRouter()

router_sendings_v1.register("", ContentViewSet, basename="contents")

urlpatterns = [
    path("", include(router_sendings_v1.urls)),
]
