"""Классы выбора для моделей приложения Sendings."""

from django.db import models


class SendingStatus(models.TextChoices):
    """Статусы отправки мерча."""

    SENT = "Sent", "Отправлено"
    ERROR = "Error", "Ошибка"


class MerchType(models.TextChoices):
    """Типы мерча."""

    SHOES = "Shoes", "Обувь"
    CLOTHING = "Clothing", "Одежда"
    MISC = "Miscellaneous", "Разное"
