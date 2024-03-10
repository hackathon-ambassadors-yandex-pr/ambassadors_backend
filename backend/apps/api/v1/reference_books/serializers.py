from apps.content.models import SocialNetwork
from apps.sendings.models import Merch
from rest_framework import serializers


class MerchSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Merch."""

    class Meta:
        model = Merch
        fields = ["id", "type", "name", "unit_price"]


class SocialNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом SocialNetwork."""

    class Meta:
        model = SocialNetwork
        fields = ["id", "name"]
