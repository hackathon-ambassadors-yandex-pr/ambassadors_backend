from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)

urlpatterns = [
    path(
        "login/",
        get_drf_spectacular_view_decorator("users")(TokenObtainPairView.as_view()),
        name="users_login",
    ),
]
