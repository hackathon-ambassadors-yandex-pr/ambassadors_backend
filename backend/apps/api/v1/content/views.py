from apps.api.v1.content.serializers import ContentSerializer, PartialContentSerializer
from apps.content.models import Content
from rest_framework import viewsets


class ContentViewSet(viewsets.ModelViewSet):
    """Обработчик запросов эндпоинтов Content."""

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContentSerializer
        elif self.action == 'partial_update':
            return PartialContentSerializer
