from rest_framework import viewsets

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.api.v1.users.serializers import UserSerializer
from apps.users.models import User


@get_drf_spectacular_view_decorator("users")
class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с данными пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
