from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/v1/users/login/", TokenObtainPairView.as_view(), name="api_token_auth"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
