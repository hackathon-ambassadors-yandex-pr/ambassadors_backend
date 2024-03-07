"""Классы выбора для моделей приложения Sendings."""

from django.db import models


class SendingStatus(models.TextChoices):
    """Статусы отправки мерча."""

    SENT = "Отправлено"
    ERROR = "Ошибка"


class MerchType(models.TextChoices):
    """Типы мерча."""

    SHOES = "Обувь"
    CLOTHING = "Одежда"
    MISC = "Разное"
