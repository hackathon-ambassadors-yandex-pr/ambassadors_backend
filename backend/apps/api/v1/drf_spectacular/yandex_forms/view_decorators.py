from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status

from apps.api.v1.drf_spectacular.core.serializers import Response400Serializer
from apps.api.v1.yandex_forms.serializers import (
    AmbassadorFormSerializer,
    ContentFormSerializer,
)

YANDEX_FORMS_VIEW_DECORATORS = {
    "process_ambassador_form": extend_schema(
        tags=("Yandex Forms",),
        request=AmbassadorFormSerializer,
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(response=None),
            status.HTTP_400_BAD_REQUEST: Response400Serializer,
        },
    ),
    "process_content_form": extend_schema(
        tags=("Yandex Forms",),
        request=ContentFormSerializer,
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(response=None),
            status.HTTP_400_BAD_REQUEST: Response400Serializer,
        },
    ),
}
