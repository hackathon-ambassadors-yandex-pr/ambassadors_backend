from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import UserViewSet

router = DefaultRouter()
router.register(r"", UserViewSet)

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="users_login"),
    path(
        "me/", UserViewSet.as_view({"get": "retrieve", "put": "update"}), name="user-me"
    ),
]


urlpatterns += router.urls
