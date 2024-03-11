from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.api.v1.drf_spectacular.core.serializers import (
    Response400Serializer,
    Response401Serializer,
)
from apps.api.v1.users.serializers import UserSerializer

USERS_VIEW_DECORATORS = {
    "TokenObtainPairView": extend_schema_view(
        post=extend_schema(
            description="Получение JWT токенов",
            tags=("Users",),
            responses={
                status.HTTP_200_OK: TokenObtainPairSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "UserViewSet": extend_schema_view(
        create=extend_schema(
            description="Создание профайла нового пользователя",
            tags=("Users",),
            responses={
                status.HTTP_201_CREATED: UserSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        retrieve=extend_schema(
            description="Получение данных пользователя",
            tags=("Users",),
            responses={
                status.HTTP_200_OK: UserSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        partial_update=extend_schema(
            description="Изменение данных пользователя",
            tags=("Users",),
            responses={
                status.HTTP_200_OK: UserSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
}
