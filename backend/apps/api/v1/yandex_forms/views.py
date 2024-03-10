"""Обработчики запросов на эндпоинты yandex_forms/ API v1."""

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.api.v1.yandex_forms.serializers import (
    AmbassadorFormSerializer,
    ContentFormSerializer,
)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@get_drf_spectacular_view_decorator("yandex_forms")
@api_view(("POST",))
@permission_classes((AllowAny,))
def process_ambassador_form(request):
    """Обработчик запросов на эндпоинт ambassador_forms/."""
    serializer = AmbassadorFormSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)


@get_drf_spectacular_view_decorator("yandex_forms")
@api_view(("POST",))
@permission_classes((AllowAny,))
def process_content_form(request):
    """Обработчик запросов на эндпоинт content_forms/."""
    serializer = ContentFormSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
