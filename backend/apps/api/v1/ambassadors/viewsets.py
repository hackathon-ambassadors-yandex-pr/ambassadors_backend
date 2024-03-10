from rest_framework import mixins, viewsets


class CreateListRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet actions: create, list, retrieve, update."""

    http_method_names = ("post", "get", "put", "head", "options")
