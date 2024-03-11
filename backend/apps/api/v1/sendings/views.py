"""Обработчики запросов на эндпоинты Sendings API v1."""

from rest_framework.permissions import IsAuthenticated

from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.api.v1.sendings.permissions import SendingStatusIsSentOrReadOnly
from apps.api.v1.sendings.serializers import (
    CreateSendingSerializer,
    ListSendingSerializer,
    PartialUpdateSendingSerializer,
    RetrieveSendingSerializer,
)
from apps.api.v1.sendings.viewsets import CreateListRetrievePartialUpdateViewSet
from apps.sendings.models import Sending


@get_drf_spectacular_view_decorator("sendings")
class SendingViewSet(CreateListRetrievePartialUpdateViewSet):
    """Обработчик запросов на эндпоинты Sendings."""

    queryset = Sending.objects.all()
    permission_classes = (IsAuthenticated, SendingStatusIsSentOrReadOnly)

    def get_serializer_class(self):
        if self.action == "create":
            return CreateSendingSerializer
        if self.action == "list":
            return ListSendingSerializer
        if self.action == "retrieve":
            return RetrieveSendingSerializer
        return PartialUpdateSendingSerializer
