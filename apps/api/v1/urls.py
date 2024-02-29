from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="api_token_auth"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
