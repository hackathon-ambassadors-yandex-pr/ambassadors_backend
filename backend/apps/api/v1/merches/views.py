"""Обработчики запросов на эндпоинты Merches API v1."""

from apps.api.v1.merches.serializers import (
    CreateListMerchSerializer,
    PartialUpdateMerchSerializer,
)
from apps.api.v1.merches.viewsets import CreateListPartialUpdateViewSet
from apps.sendings.models import Merch


class MerchCreateListPartialUpdateViewSet(CreateListPartialUpdateViewSet):
    """Обработчик запросов для получения списка объектов Merch и их создания и изменения."""

    queryset = Merch.objects.all()

    def get_serializer_class(self):
        if self.action == "partial_update":
            return PartialUpdateMerchSerializer

        return CreateListMerchSerializer
