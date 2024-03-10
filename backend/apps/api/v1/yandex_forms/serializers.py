"""Сериализаторы для обработки данных форм."""

from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from apps.ambassadors.choice_classes import EducationTarget
from apps.ambassadors.models import Address, Ambassador, Program, Target
from apps.content.choice_classes import ContentStatus
from apps.content.models import Content, ContentFile


class AddressFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных адреса из формы амбассадора."""

    class Meta:
        model = Address
        fields = ("country", "city", "address", "code")


class AmbassadorFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных формы амбассадора."""

    current_address = AddressFormSerializer(write_only=True)
    program = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Program.objects.all(),
    )
    targets = serializers.SlugRelatedField(
        slug_field="name",
        many=True,
        queryset=Target.objects.all(),
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


class FileFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки файлов из формы контента."""

    class Meta:
        model = ContentFile
        fields = (
            "id",
            "file",
        )


class ContentFormSerializer(serializers.ModelSerializer):
    """Сериализатор для обработки данных формы контента."""

    content_files = FileFormSerializer(many=True, required=False)

    class Meta:
        model = Content
        fields = (
            "id",
            "first_name_from_form",
            "last_name_from_form",
            "telegram_link_from_form",
            "link",
            "guide_check",
            "content_files",
            "ambassador",
            "status",
            "uploaded_at",
        )
        extra_kwargs = {
            "first_name_from_form": {"required": True},
            "last_name_from_form": {"required": True},
            "telegram_link_from_form": {"required": True},
        }
        read_only_fields = (
            "ambassador",
            "status",
            "uploaded_at",
        )

    @transaction.atomic
    def create(self, validated_data):
        content_files = validated_data.pop("content_files", None)
        ambassador = Ambassador.objects.filter(
            telegram_link=validated_data["telegram_link_from_form"]
        ).first()

        if ambassador is None:
            content = Content.objects.create(**validated_data, status=ContentStatus.TBC)
        else:
            content = Content.objects.create(
                ambassador=ambassador,
                link=validated_data["link"],
                guide_check=validated_data["guide_check"],
            )

        if content_files is not None:
            ContentFile.objects.bulk_create(
                (
                    ContentFile(
                        content=content,
                        file=item["file"],
                    )
                    for item in content_files
                )
            )

        return content
