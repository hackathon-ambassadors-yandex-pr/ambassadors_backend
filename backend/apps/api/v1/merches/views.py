"""Обработчики запросов на эндпоинты Merches API v1."""

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.api.v1.merches.serializers import (
    CreateListMerchSerializer,
    PartialUpdateMerchSerializer,
)
from apps.api.v1.merches.viewsets import CreateListPartialUpdateViewSet
from apps.sendings.models import Merch


@get_drf_spectacular_view_decorator("merches")
class MerchCreateListPartialUpdateViewSet(CreateListPartialUpdateViewSet):
    """Обработчик запросов для получения списка объектов Merch и их создания и изменения."""

    queryset = Merch.objects.all()

    def get_serializer_class(self):
        if self.action == "partial_update":
            return PartialUpdateMerchSerializer

        return CreateListMerchSerializer
