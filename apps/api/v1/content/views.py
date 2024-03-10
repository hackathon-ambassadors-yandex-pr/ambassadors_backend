from rest_framework import viewsets
from apps.content.models import Content, ContentFile, SocialNetwork
from .serializers import (
    ContentSerializer,
    ContentFileSerializer,
    SocialNetworkSerializer
)

class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()
    serializer_class = SocialNetworkSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentFileViewSet(viewsets.ModelViewSet):
    queryset = ContentFile.objects.all()
    serializer_class = ContentFileSerializer
