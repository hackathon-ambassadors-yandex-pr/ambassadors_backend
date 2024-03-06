"""Классы для проверки прав на запросы на эндпоинты группы Sendings."""

from rest_framework import permissions

from apps.sendings.choice_classes import SendingStatus


class SendingStatusIsSentOrReadOnly(permissions.BasePermission):
    """Проверка прав на доступ к объекту Sending."""

    message = "Не допускается изменение объекта Sending, статус которого не 'Sent'."

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.status == SendingStatus.SENT
        )
