from rest_framework import serializers

from apps.ambassadors.models import Ambassador
from apps.content.models import Content, ContentFile


class AmbassadorContentBaseSerializer(serializers.ModelSerializer):
    """Сериализатор для поля ambassador в ContentBaseSerialiser."""

    class Meta:
        model = Ambassador
        fields = ("id", "first_name", "last_name", "telegram_link")


class ContentBaseSerialiser(serializers.ModelSerializer):
    """Базовый сериализатор для работы с объектами Content."""

    ambassador = AmbassadorContentBaseSerializer()
    social_network = serializers.CharField(source="social_network.name")

    class Meta:
        model = Content
        fields = (
            "id",
            "link",
            "status",
            "guide_check",
            "social_network",
            "first_name_from_form",
            "last_name_from_form",
            "telegram_link_from_form",
            "ambassador",
        )


class ListContentSerializer(ContentBaseSerialiser):
    """Сериализатор для получения списка объектов Content."""

    files_exist = serializers.BooleanField()

    class Meta:
        model = Content
        fields = (*ContentBaseSerialiser.Meta.fields, "files_exist", "uploaded_at")


class ContentFileSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектами ContentFile."""

    class Meta:
        model = ContentFile
        fields = ("id", "file")


class RetrieveContentSerializer(ContentBaseSerialiser):
    """Сериализатор для получения подробной информации об объекте Content."""

    content_files = ContentFileSerializer(many=True)

    class Meta:
        model = Content
        fields = (*ContentBaseSerialiser.Meta.fields, "user_comment", "content_files")


class PartialUpdateContentSerializer(serializers.ModelSerializer):
    """Сериализатор для частичного обновления объекта Content."""

    class Meta:
        model = Content
        fields = (
            "social_network",
            "status",
            "guide_check",
            "user_comment",
            "ambassador",
        )

    def validate_ambassador(self, value):
        if self.instance.ambassador is not None:
            raise serializers.ValidationError(
                "You cannot change value of this field , "
                "because current value of this field is not None."
            )
        return value

    def update(self, instance, validated_data):
        if validated_data.get("ambassador") is not None:
            validated_data.update(
                {
                    "first_name_from_form": "",
                    "last_name_from_form": "",
                    "telegram_link_from_form": "",
                }
            )
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        return RetrieveContentSerializer(instance).data
