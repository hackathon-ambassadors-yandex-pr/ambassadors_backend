"""Сериализаторы для обработки данных форм."""

from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from apps.ambassadors.choice_classes import EducationTarget
from apps.ambassadors.models import Address, Ambassador, Program, Target
from apps.api.v1.yandex_forms.fields import ContentFormBooleanField
from apps.content.choice_classes import ContentStatus
from apps.content.models import Content


class AddressFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных адреса из формы амбассадора."""

    class Meta:
        model = Address
        fields = ("country", "city", "address", "code")


class AmbassadorFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных формы амбассадора."""

    current_address = AddressFormSerializer(write_only=True)
    program = serializers.SlugRelatedField(
        queryset=Program.objects.all(),
        slug_field="name",
    )
    targets = serializers.PrimaryKeyRelatedField(
        queryset=Target.objects.all(),
        many=True,
    )

    class Meta:
        model = Ambassador
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "gender",
            "program",
            "current_address",
            "email",
            "mobile_phone",
            "telegram_link",
            "education",
            "work_place",
            "education_target",
            "education_target_own",
            "targets",
            "blog_link",
            "clothing_size",
            "shoe_size",
            "comment_ambassador",
        )

    def validate(self, attrs):
        education_target = attrs["education_target"]
        education_target_own = attrs["education_target_own"]

        if education_target == EducationTarget.OTHER and not education_target_own:
            raise serializers.ValidationError(
                f"if education_target == {EducationTarget.OTHER}, "
                f"then education_target_own field cannot be empty."
            )
        if education_target != EducationTarget.OTHER and education_target_own:
            raise serializers.ValidationError(
                f"if education_target != {EducationTarget.OTHER}, "
                f"then education_target_own field should be empty."
            )

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        current_address = validated_data.pop("current_address")
        ambassador = super().create(validated_data)
        Address.objects.create(
            ambassador=ambassador, replaced_at=timezone.now(), **current_address
        )
        return ambassador


class ContentFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных формы контента."""

    guide_check = ContentFormBooleanField(default=False)

    class Meta:
        model = Content
        fields = (
            "id",
            "first_name_from_form",
            "last_name_from_form",
            "telegram_link_from_form",
            "link",
            "guide_check",
        )
        extra_kwargs = {
            "first_name_from_form": {"required": True},
            "last_name_from_form": {"required": True},
            "telegram_link_from_form": {"required": True},
        }

    @transaction.atomic
    def create(self, validated_data):
        ambassador = Ambassador.objects.filter(
            telegram_link=validated_data["telegram_link_from_form"]
        ).first()
        if ambassador is None:
            return Content.objects.create(**validated_data, status=ContentStatus.TBC)

        return Content.objects.create(
            ambassador=ambassador,
            link=validated_data["link"],
            guide_check=validated_data["guide_check"],
        )
