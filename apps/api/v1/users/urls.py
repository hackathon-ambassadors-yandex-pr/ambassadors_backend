from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from .views import UserViewSet

router = DefaultRouter()

router.register(r"", UserViewSet)

urlpatterns = [
    path(
        "login/",
        get_drf_spectacular_view_decorator("users")(TokenObtainPairView.as_view()),
        name="users_login",
    ),
    path(
        "me/",
        UserViewSet.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="users-me",
    ),
]
