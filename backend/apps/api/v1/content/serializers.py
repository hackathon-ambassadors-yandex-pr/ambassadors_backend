from apps.content.models import Content
from rest_framework import serializers


class ContentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Content."""

    class Meta:
        model = Content
        fields = ["id", "uploaded_at", "social_network", "status", "guide_check", "link", "ambassador",]


class PartialContentSerializer(serializers.ModelSerializer):
    """Сериализатор для изменения данных контента."""

    class Meta:
        model = Content
        fields = ["social_network", "status", "guide_check", "user_comment"] 

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
