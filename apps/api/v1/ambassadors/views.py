from apps.ambassadors.models import Ambassador
from apps.api.v1.ambassadors.serializers import (
    CreateUpdateAmbassadorSerializer,
    ListAmbassadorSerializer,
    RetrieveAmbassadorSerializer,
)
from apps.api.v1.ambassadors.viewsets import CreateListRetrieveUpdateViewSet


class AmbassadorViewSet(CreateListRetrieveUpdateViewSet):
    """Обработчик запросов эндпоинтов Ambassadors."""

    queryset = Ambassador.objects.select_related("status", "program")

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUpdateAmbassadorSerializer
        if self.action == "list":
            return ListAmbassadorSerializer
        if self.action == "retrieve":
            return RetrieveAmbassadorSerializer
        return CreateUpdateAmbassadorSerializer
