"""Сериализаторы для работы с ресурсами приложения Sendings."""

from django.db import IntegrityError, transaction
from rest_framework import serializers

from apps.ambassadors.models import Address, Ambassador
from apps.sendings.models import Sending, SendingToMerch


class SendingToMerchSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектами SendingToMerch."""

    class Meta:
        model = SendingToMerch
        fields = ("merch", "size", "quantity", "unit_price")
        read_only_fields = ("unit_price",)


class CreateSendingSerializer(serializers.ModelSerializer):
    """Сериализатор для создания объекта Sending."""

    ambassador = serializers.PrimaryKeyRelatedField(queryset=Ambassador.objects.all())
    sending_merches = SendingToMerchSerializer(many=True)

    class Meta:
        model = Sending
        fields = ("ambassador", "user_comment", "sending_merches")
        extra_kwargs = {"user_comment": {"required": True}}

    def validate_merches(self, value):
        if not value:
            raise serializers.ValidationError("Field value cannot be empty list.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        address = validated_data["ambassador"].addresses.filter(is_current=True).first()
        sending = Sending.objects.create(
            address=address,
            user_comment=validated_data["user_comment"],
        )
        self.add_merches_to_sending(sending, validated_data["sending_merches"])
        return sending

    @staticmethod
    def add_merches_to_sending(sending, sending_merches):
        try:
            SendingToMerch.objects.bulk_create(
                (
                    SendingToMerch(
                        sending=sending,
                        **sending_merch,
                        unit_price=sending_merch["merch"].unit_price,
                    )
                    for sending_merch in sending_merches
                ),
            )
        except IntegrityError:
            raise serializers.ValidationError(
                {"sending_merch": "Merch with size must be unique in this sending."}
            )

    def to_representation(self, instance):
        return RetrieveSendingSerializer(instance).data


class AmbassadorBriefSerializer(serializers.ModelSerializer):
    """Сериализатор объекта Ambassador для использования в ListSendingSerializer."""

    class Meta:
        model = Ambassador
        fields = ("id", "first_name", "last_name")


class SendingMerchSerializer(serializers.Serializer):
    """Сериализатор для получения значения поля sending_merches в ListSendingSerializer."""

    id = serializers.IntegerField(source="merch.id")
    name = serializers.CharField(source="merch.name")


class ListSendingSerializer(serializers.ModelSerializer):
    """Сериализатор списка объектов Sending."""

    ambassador = AmbassadorBriefSerializer(source="address.ambassador")
    sending_merches = SendingMerchSerializer(many=True, source="sending_to_merches")

    class Meta:
        model = Sending
        fields = ("id", "created_at", "status", "ambassador", "sending_merches")


class AmbassadorSerializer(serializers.ModelSerializer):
    """Сериализатор объекта Ambassador для использования в RetrieveSendingSerializer."""

    class Meta:
        model = Ambassador
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "clothing_size",
            "shoe_size",
            "telegram_link",
            "email",
            "mobile_phone",
        )


class SendingAddressSerializer(serializers.ModelSerializer):
    """Сериализатор объекта Address для использования в RetrieveSendingSerializer."""

    class Meta:
        model = Address
        fields = ("id", "code", "country", "city", "address")


class RetrieveSendingSerializer(serializers.ModelSerializer):
    """Сериализатор объекта Sending."""

    address = SendingAddressSerializer()
    ambassador = AmbassadorSerializer(source="address.ambassador")
    sending_merches = SendingToMerchSerializer(many=True, source="sending_to_merches")

    class Meta:
        model = Sending
        fields = (
            "id",
            "reg_number",
            "status",
            "user_comment",
            "address",
            "ambassador",
            "sending_merches",
        )


class PartialUpdateSendingSerializer(serializers.ModelSerializer):
    """Сериализатор для частичного обновления объекта Sending."""

    class Meta:
        model = Sending
        fields = ("id", "status", "user_comment")

    def to_representation(self, instance):
        return RetrieveSendingSerializer(instance).data
