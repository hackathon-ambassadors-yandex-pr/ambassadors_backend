from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.v1.drf_spectacular.core.serializers import (
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)
from apps.api.v1.drf_spectacular.sendings.serializers import (
    SendingUpdateResponse403Serializer,
)
from apps.api.v1.sendings.serializers import (
    ListSendingSerializer,
    RetrieveSendingSerializer,
)

SENDINGS_VIEW_DECORATORS = {
    "SendingViewSet": extend_schema_view(
        create=extend_schema(
            description="Новая отправка мерча амбассадору (карточка)",
            tags=("Sendings",),
            responses={
                status.HTTP_201_CREATED: RetrieveSendingSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        list=extend_schema(
            description="Список отправок мерча амбассадорам (экран Мерч)",
            tags=("Sendings",),
            responses={
                status.HTTP_200_OK: ListSendingSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        retrieve=extend_schema(
            description="Данные отправки мерча амбассадору (карточка)",
            tags=("Sendings",),
            responses={
                status.HTTP_200_OK: RetrieveSendingSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        partial_update=extend_schema(
            description="Обновление данных отправки мерча амбассадору (карточка)",
            tags=("Sendings",),
            responses={
                status.HTTP_200_OK: RetrieveSendingSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_403_FORBIDDEN: SendingUpdateResponse403Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
