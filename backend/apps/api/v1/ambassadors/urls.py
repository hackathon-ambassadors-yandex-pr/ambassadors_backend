from apps.api.v1.ambassadors.views import AmbassadorViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_ambassadors = DefaultRouter()

router_ambassadors.register("", AmbassadorViewSet, basename="ambassadors")

urlpatterns = [
    path("", include(router_ambassadors.urls)),
]
