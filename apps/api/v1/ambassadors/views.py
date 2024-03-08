from django.db.models import Count

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

    def get_queryset(self):
        queryset = Ambassador.objects.all().select_related("program")
        if self.action == "list":
            queryset = queryset.annotate(content_count=Count("contents"))
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return ListAmbassadorSerializer
        if self.action == "retrieve":
            return RetrieveAmbassadorSerializer
        return CreateUpdateAmbassadorSerializer
