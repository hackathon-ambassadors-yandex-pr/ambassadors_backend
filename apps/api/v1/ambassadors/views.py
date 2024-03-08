from apps.ambassadors.models import Ambassador
from apps.api.v1.ambassadors.serializers import (
    CreateUpdateAmbassadorSerializer,
    ListAmbassadorSerializer,
    RetrieveAmbassadorSerializer,
)
from apps.api.v1.ambassadors.viewsets import CreateListRetrieveUpdateViewSet
from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)


@get_drf_spectacular_view_decorator("ambassadors")
class AmbassadorViewSet(CreateListRetrieveUpdateViewSet):
    """Обработчик запросов эндпоинтов Ambassadors."""

    queryset = Ambassador.objects.all().select_related("program")

    def get_serializer_class(self):
        if self.action == "list":
            return ListAmbassadorSerializer
        if self.action == "retrieve":
            return RetrieveAmbassadorSerializer
        return CreateUpdateAmbassadorSerializer
