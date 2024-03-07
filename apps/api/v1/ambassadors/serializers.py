from rest_framework import serializers

from apps.ambassadors.models import (
    Address,
    Ambassador,
    Program,
    Promocode,
    Target,
)
from apps.content.models import Content
from apps.sendings.models import Sending


class AddressSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Address."""

    class Meta:
        model = Address
        fields = ("id", "country", "city", "address", "code", "is_current")


class ProgramSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Program."""

    class Meta:
        model = Program
        fields = ("id", "name")


class PromocodeSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Promocode."""

    class Meta:
        model = Promocode
        fields = ("id", "value", "is_current")


class TargetSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Target."""

    class Meta:
        model = Target
        fields = ("id", "name")


class ContentSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Content."""

    class Meta:
        model = Content
        fields = ("id", "uploaded_at", "status", "link")


class SendingSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектом Sending."""

    class Meta:
        model = Sending
        fields = ("id", "created_at", "status")


class RetrieveAmbassadorSerializer(serializers.ModelSerializer):
    """Сериализатор для возвращения объекта Ambassador."""

    program = ProgramSerializer(read_only=True)
    targets = TargetSerializer(many=True, read_only=True)
    current_address = AddressSerializer(read_only=True)
    current_promocode = PromocodeSerializer(read_only=True)
    contents = ContentSerializer(many=True, read_only=True)
    sendings = SendingSerializer(many=True, read_only=True)

    class Meta:
        model = Ambassador
        fields = (
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "gender",
            "status",
            "registration_date",
            "user_comment",
            "clothing_size",
            "shoe_size",
            "telegram_link",
            "email",
            "mobile_phone",
            "blog_link",
            "education",
            "work_place",
            "education_target",
            "education_target_own",
            "onboarding_date",
            "guide_date",
            "comment_ambassador",
            "program",
            "targets",
            "current_address",
            "current_promocode",
            "contents",
            "sendings",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_promocode = Promocode.objects.filter(
            ambassador=instance, is_current=True
        ).first()
        current_address = Address.objects.filter(
            ambassador=instance, is_current=True
        ).first()

        if current_address:
            representation["current_address"] = AddressSerializer(current_address).data
            sendings = Sending.objects.filter(address=current_address)
            representation["sendings"] = SendingSerializer(sendings, many=True).data
        else:
            representation["current_address"] = None
            representation["sendings"] = []

        if current_promocode:
            representation["current_promocode"] = PromocodeSerializer(
                current_promocode
            ).data
        else:
            representation["current_promocode"] = None

        return representation


class CreateUpdateAmbassadorSerializer(serializers.ModelSerializer):
    """Сериализатор для создания или изменения объекта Ambassador."""

    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())
    targets = serializers.PrimaryKeyRelatedField(
        queryset=Target.objects.all(), many=True
    )
    current_address = AddressSerializer()
    current_promocode = PromocodeSerializer()

    class Meta:
        model = Ambassador
        fields = (
            "last_name",
            "first_name",
            "middle_name",
            "gender",
            "status",
            "user_comment",
            "clothing_size",
            "shoe_size",
            "telegram_link",
            "email",
            "mobile_phone",
            "blog_link",
            "education",
            "work_place",
            "education_target",
            "education_target_own",
            "onboarding_date",
            "guide_date",
            "comment_ambassador",
            "program",
            "targets",
            "current_address",
            "current_promocode",
        )

    def create(self, validated_data):
        targets_data = validated_data.pop("targets", None)
        current_address_data = validated_data.pop("current_address", None)
        current_promocode_data = validated_data.pop("current_promocode", None)

        ambassador = Ambassador.objects.create(**validated_data)

        for target in targets_data:
            ambassador.targets.add(target)

        Address.objects.create(ambassador=ambassador, **current_address_data)
        Promocode.objects.create(ambassador=ambassador, **current_promocode_data)

        return ambassador

    def update(self, instance, validated_data):
        targets = validated_data.pop("targets")
        instance.targets.set(targets)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        current_address_data = validated_data.pop("current_address", None)
        if current_address_data:
            current_address = Address.objects.filter(
                ambassador=instance, is_current=True
            ).first()
            if current_address:
                for key, val in current_address_data.items():
                    setattr(current_address, key, val)
                current_address.save()
            else:
                Address.objects.create(ambassador=instance, **current_address_data)

        current_promocode_data = validated_data.pop("current_promocode", None)
        if current_promocode_data:
            current_promocode = Promocode.objects.filter(
                ambassador=instance, is_current=True
            ).first()
            if current_promocode:
                for key, val in current_promocode_data.items():
                    setattr(current_promocode, key, val)
                current_promocode.save()
            else:
                Promocode.objects.create(ambassador=instance, **current_promocode_data)

        instance.save()
        return instance

    def to_representation(self, instance):
        return RetrieveAmbassadorSerializer(instance).data


class ListAmbassadorSerializer(serializers.ModelSerializer):
    """Сериализатор для возвращения списка объектов Ambassadors."""

    current_promocode = PromocodeSerializer(read_only=True)
    content_count = serializers.SerializerMethodField()

    class Meta:
        model = Ambassador
        fields = (
            "id",
            "first_name",
            "last_name",
            "registration_date",
            "status",
            "telegram_link",
            "current_promocode",
            "content_count",
        )

    def get_content_count(self, obj):
        return obj.contents.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        current_promocode = Promocode.objects.filter(
            ambassador=instance, is_current=True
        ).first()

        if current_promocode:
            representation["current_promocode"] = PromocodeSerializer(
                current_promocode
            ).data
        else:
            representation["current_promocode"] = None
        return representation
