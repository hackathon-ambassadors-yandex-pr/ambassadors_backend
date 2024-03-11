from rest_framework import serializers

from apps.ambassadors.models import Address, Ambassador
from apps.content.models import SocialNetwork
from apps.sendings.models import Merch


class AddressReferenceBooksSerializer(serializers.ModelSerializer):
    """Сериализатор для поля address в AmbassadorReferenceBooksSerializer."""

    class Meta:
        model = Address
        fields = ("id", "country", "city", "address", "code")


class AmbassadorReferenceBooksSerializer(serializers.ModelSerializer):
    """Сериализатор списка амбассадоров для выбора в новой отправке мерча"""

    current_address = AddressReferenceBooksSerializer()

    class Meta:
        model = Ambassador
        fields = (
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "clothing_size",
            "shoe_size",
            "telegram_link",
            "email",
            "mobile_phone",
            "current_address",
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        current_address = Address.objects.filter(
            ambassador=instance, is_current=True
        ).first()
        ret["current_address"] = AddressReferenceBooksSerializer(current_address).data
        return ret


class MerchReferenceBooksSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Merch."""

    class Meta:
        model = Merch
        fields = ("id", "type", "name", "unit_price")


class SocialNetworkReferenceBooksSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом SocialNetwork."""

    class Meta:
        model = SocialNetwork
        fields = ("id", "name")
