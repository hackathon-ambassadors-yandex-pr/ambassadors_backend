from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя."""

    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "middle_name",
            "email",
            "registration_date",
            "avatar",
        ]
