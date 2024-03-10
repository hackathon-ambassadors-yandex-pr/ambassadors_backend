from rest_framework import serializers

from apps.ambassadors.choice_classes import AmbassadorStatus
from apps.content.models import SocialNetwork
from apps.sendings.models import Merch


class AmbassadorStatusSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом AmbassadorStatus."""

    class Meta:
        model = AmbassadorStatus
        fields = ["id", "name"]


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
