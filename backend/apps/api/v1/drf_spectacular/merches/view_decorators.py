from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from apps.api.v1.drf_spectacular.core.serializers import (
    Response400Serializer,
    Response401Serializer,
    Response404Serializer,
)
from apps.api.v1.merches.serializers import (
    CreateListMerchSerializer,
    PartialUpdateMerchSerializer,
)

MERCHES_VIEW_DECORATORS = {
    "MerchCreateListPartialUpdateViewSet": extend_schema_view(
        create=extend_schema(
            description="Новый мерч.",
            tags=("Merches",),
            responses={
                status.HTTP_201_CREATED: CreateListMerchSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        list=extend_schema(
            description="Список мерча.",
            tags=("Merches",),
            responses={
                status.HTTP_200_OK: CreateListMerchSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
        partial_update=extend_schema(
            description="Обновление данных мерча.",
            tags=("Merches",),
            responses={
                status.HTTP_200_OK: PartialUpdateMerchSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
                status.HTTP_404_NOT_FOUND: Response404Serializer,
            },
        ),
    ),
}
