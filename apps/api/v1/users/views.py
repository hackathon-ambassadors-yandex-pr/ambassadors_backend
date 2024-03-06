from rest_framework import viewsets

from apps.api.v1.users.serializers import UserSerializer
from apps.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с данными пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
