from apps.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""

    class Meta:
        model = User
        fields = [
            "id",
            "last_name",
            "first_name",
            "middle_name",
            "email",
            "registration_date",
            "avatar",
            "password",
        ]
        read_only_fields = ["registration_date"]
        extra_kwargs = {"password": {"write_only": True}}
