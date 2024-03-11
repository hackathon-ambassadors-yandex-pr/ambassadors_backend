"""Сериализаторы для работы с ресурсом Merch приложения Sendings."""

from rest_framework import serializers

from apps.sendings.models import Merch


class CreateListMerchSerializer(serializers.ModelSerializer):
    """Сериализатор для получения списка объектов Merch и их создания."""

    class Meta:
        model = Merch
        fields = ("id", "name", "type", "size", "unit_price", "quantity")


class PartialUpdateMerchSerializer(serializers.ModelSerializer):
    """Сериализатор для частичного обновления объекта Merch."""

    class Meta:
        model = Merch
        fields = ("id", "name", "type", "size", "unit_price", "quantity")
        read_only_fields = ("quantity",)
