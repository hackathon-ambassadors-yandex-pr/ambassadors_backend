from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ContentViewSet, ContentFileViewSet, SocialNetworkViewSet

router = DefaultRouter()
router.register(r'social-networks', SocialNetworkViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'content-files', ContentFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
