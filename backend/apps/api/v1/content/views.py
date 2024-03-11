from django.db.models import Exists, OuterRef

from apps.api.v1.content.serializers import (
    ListContentSerializer,
    PartialUpdateContentSerializer,
    RetrieveContentSerializer,
)
from apps.api.v1.content.viewsets import ListRetrievePartialUpdateViewSet
from apps.api.v1.drf_spectacular.custom_decorators import (
    get_drf_spectacular_view_decorator,
)
from apps.content.models import Content, ContentFile


@get_drf_spectacular_view_decorator("contents")
class ContentListRetrievePartialUpdateViewSet(ListRetrievePartialUpdateViewSet):
    """Обработчик запросов на эндпоинты Contents."""

    def get_queryset(self):
        queryset = Content.objects.all()

        if self.action == "partial_update":
            return queryset

        queryset = queryset.select_related("ambassador", "social_network")

        if self.action == "list":
            files_exist_subquery = ContentFile.objects.filter(content=OuterRef("pk"))
            return queryset.annotate(files_exist=Exists(files_exist_subquery))

        return queryset.prefetch_related("content_files")

    def get_serializer_class(self):
        if self.action == "partial_update":
            return PartialUpdateContentSerializer
        if self.action == "list":
            return ListContentSerializer
        return RetrieveContentSerializer
