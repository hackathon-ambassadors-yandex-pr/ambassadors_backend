"""Базовые классы вьюсетов для обработчиков запросов на эндпоинты Sendings API v1."""

from rest_framework import mixins, viewsets


class CreateListRetrievePartialUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet предоставляющий actions: create, list, retrieve, partial_update."""

    http_method_names = ("post", "get", "patch", "head", "options")
