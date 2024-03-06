from django.db import models

class ContentStatus(models.TextChoices):
    """Статус контента."""

NEW = "New", "Новый"
RESPOND = "Respond", "Соответствует"
NOT_RESPOND = "Not respond", "Не соответствует"
TBC = "TBC", "Уточняется"
