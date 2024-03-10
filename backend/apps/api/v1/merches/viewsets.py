"""Базовые классы вьюсетов для обработчиков запросов на эндпоинты Merches API v1."""

from rest_framework import mixins, viewsets


class CreateListPartialUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet предоставляющий actions: create, list, partial_update."""

    http_method_names = ("post", "get", "patch", "head", "options")
