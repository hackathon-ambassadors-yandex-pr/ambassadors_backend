"""Базовые классы вьюсетов для обработчиков запросов на эндпоинты Contents API v1."""

from rest_framework import mixins, viewsets


class ListRetrievePartialUpdateViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet предоставляющий actions: list, retrieve, partial_update."""

    http_method_names = ("get", "patch", "head", "options")
