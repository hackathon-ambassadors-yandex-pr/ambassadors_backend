from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.v1.content.serializers import (
    ListContentSerializer,
    PartialUpdateContentSerializer,
    RetrieveContentSerializer,
)
from apps.api.v1.drf_spectacular.core.serializers import (
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)

CONTENTS_VIEW_DECORATORS = {
    "ContentListRetrievePartialUpdateViewSet": extend_schema_view(
        list=extend_schema(
            description="Список контента амбассадоров (экран Контент)",
            tags=("Contents",),
            responses={
                status.HTTP_200_OK: ListContentSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        retrieve=extend_schema(
            description="Данные контента амбассадора (карточка)",
            tags=("Contents",),
            responses={
                status.HTTP_200_OK: RetrieveContentSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
        partial_update=extend_schema(
            description="Обновление данных контента амбассадора (карточка)",
            tags=("Contents",),
            responses={
                status.HTTP_200_OK: PartialUpdateContentSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
