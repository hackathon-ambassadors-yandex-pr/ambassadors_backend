from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.v1.ambassadors.serializers import (
    ListAmbassadorSerializer,
    RetrieveAmbassadorSerializer,
)
from apps.api.v1.drf_spectacular.core.serializers import (
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)

AMBASSADORS_VIEW_DECORATORS = {
    "AmbassadorViewSet": extend_schema_view(
        create=extend_schema(
            description="Новый амбассадор (карточка)",
            tags=("Ambassadors",),
            responses={
                status.HTTP_201_CREATED: RetrieveAmbassadorSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        list=extend_schema(
            description="Список амбассадоров (экран Амбассадоры)",
            tags=("Ambassadors",),
            responses={
                status.HTTP_200_OK: ListAmbassadorSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        retrieve=extend_schema(
            description="Данные амбассадора (карточка) и история контента / отправок мерча",
            tags=("Ambassadors",),
            responses={
                status.HTTP_200_OK: RetrieveAmbassadorSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        update=extend_schema(
            description="Обновление данных амбассадора (карточка)",
            tags=("Ambassadors",),
            responses={
                status.HTTP_200_OK: RetrieveAmbassadorSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
