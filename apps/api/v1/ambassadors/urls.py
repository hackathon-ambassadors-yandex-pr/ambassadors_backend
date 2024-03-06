from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.ambassadors.views import (  # AmbassadorList,; AmbassadorCreate,; AmbassadorDetail,
    AmbassadorViewSet,
)

router_ambassadors = DefaultRouter()

router_ambassadors.register("", AmbassadorViewSet, basename="ambassadors")

urlpatterns = [
    path("", include(router_ambassadors.urls)),
    # path("", AmbassadorList.as_view(), name='ambassadors-list'),
    # path("create/", AmbassadorCreate.as_view(), name='ambassador-create'),
    # path('<int:pk>/', AmbassadorDetail.as_view(), name='ambassador-detail'),
]
