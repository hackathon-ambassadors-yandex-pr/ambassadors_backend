from django.db import models


class ContentStatus(models.TextChoices):
    """Статус контента."""

    NEW = "Новый"
    RESPOND = "Соответствует"
    NOT_RESPOND = "Не соответствует"
    TBC = "Уточняется", "TBC"
