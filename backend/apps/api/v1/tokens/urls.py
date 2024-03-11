from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)

urlpatterns = [
    path(
        "refresh/",
        get_drf_spectacular_view_decorator("tokens")(TokenRefreshView.as_view()),
        name="token_refresh",
    ),
]
