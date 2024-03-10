from rest_framework import serializers
from apps.content.models import Content, ContentFile, SocialNetwork

class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ("name")

class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = ("content", "file")

class ContentSerializer(serializers.ModelSerializer):
    content_files = ContentFileSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = (
            "ambassador", "first_name_from_form", "last_name_from_form",
            "telegram_link_from_form", "link", "guide_check",
            "status", "uploaded_at", "user_comment", "social_network"
        )
