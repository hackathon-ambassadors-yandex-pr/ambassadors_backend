from api.v1.ambassadors.viewsets import CreateListRetrieveUpdateViewSet

from apps.ambassadors.models import Ambassador
from apps.api.v1.ambassadors.serializers import (
    CreateUpdateAmbassadorSerializer,
    ListAmbassadorSerializer,
    RetrieveAmbassadorSerializer,
)

# class AmbassadorList(generics.ListAPIView):
#     queryset = Ambassador.objects.all()
#     serializer_class = ListAmbassadorSerializer
#
#
# class AmbassadorCreate(generics.CreateAPIView):
#     queryset = Ambassador.objects.all()
#     serializer_class = CreateAmbassadorSerializer


# class AmbassadorDetail(generics.RetrieveAPIView):
#     queryset = Ambassador.objects.all()
#     serializer_class = RetrieveAmbassadorSerializer

# class AmbassadorDetail(APIView):
#
#     def get(self, request, pk):
#         """Retrieve a single ambassador."""
#         try:
#             ambassador = Ambassador.objects.get(pk=pk)
#         except Ambassador.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = RetrieveAmbassadorSerializer(ambassador)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         """Update a single ambassador."""
#         try:
#             ambassador = Ambassador.objects.get(pk=pk)
#         except Ambassador.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = CreateAmbassadorSerializer(ambassador, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


class AmbassadorViewSet(CreateListRetrieveUpdateViewSet):
    """Обработчик запросов на эндпоинты Ambassadors."""

    queryset = Ambassador.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUpdateAmbassadorSerializer
        if self.action == "list":
            return ListAmbassadorSerializer
        if self.action == "retrieve":
            return RetrieveAmbassadorSerializer
        return CreateUpdateAmbassadorSerializer
