"""Обработчики запросов на эндпоинты yandex_forms/ API v1."""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.api.v1.yandex_forms.serializers import (
    AmbassadorFormSerializer,
    ContentFormSerializer,
)


@api_view(("POST",))
@permission_classes((AllowAny,))
def process_ambassador_form(request):
    serializer = AmbassadorFormSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(("POST",))
@permission_classes((AllowAny,))
def process_content_form(request):
    serializer = ContentFormSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)
