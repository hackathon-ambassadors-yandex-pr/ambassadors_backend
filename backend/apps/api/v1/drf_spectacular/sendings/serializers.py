from apps.api.v1.sendings.permissions import SendingStatusIsSentOrReadOnly
from rest_framework import serializers


class SendingUpdateResponse403Serializer(serializers.Serializer):
    """Ответ 403. Обновление объекта Sending не разрешено."""

    detail = serializers.CharField(default=SendingStatusIsSentOrReadOnly.message)
