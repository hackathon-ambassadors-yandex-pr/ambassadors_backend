"""Сериализаторы, описывающие ответы на запросы для использования в документации."""

from rest_framework import serializers


class Response400Serializer(serializers.Serializer):
    """Ответ 400: Некорректное значение поля или отсутствует обязательное поле."""

    field_name = serializers.ListField(
        child=serializers.CharField(
            default="Некорректное значение поля или отсутствует обязательное поле."
        )
    )


class Response401Serializer(serializers.Serializer):
    """Ответ 401: Аутентификация не пройдена."""

    detail = serializers.CharField(default="Аутентификация не пройдена.")


class Response404Serializer(serializers.Serializer):
    """Ответ 404: Объект не найден."""

    detail = serializers.CharField(default="Объект не найден.")
