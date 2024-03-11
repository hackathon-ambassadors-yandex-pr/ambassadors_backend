from rest_framework import serializers

from apps.content.models import Content


class ContentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Content."""

    class Meta:
        model = Content
        fields = [
            "id",
            "uploaded_at",
            "social_network",
            "status",
            "guide_check",
            "link",
            "ambassador",
        ]


class PartialContentSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения данных контента."""

    class Meta:
        model = Content
        fields = ["social_network", "status", "guide_check", "user_comment"]
