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


class MiscSize(models.TextChoices):
    """Разные размеры."""

    NZ = "NZ", "No size"


class ClothingSize(models.TextChoices):
    """Размеры одежды."""

    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"


class ShoesSize(models.TextChoices):
    """Размеры обуви."""

    THIRTY_FOUR = "34", "34"
    THIRTY_FIVE = "35", "35"
    THIRTY_SIX = "36", "36"
    THIRTY_SEVEN = "37", "37"
    THIRTY_EIGHT = "38", "38"
    THIRTY_NINE = "39", "39"
    FOURTY = "40", "40"
    FOURTY_ONE = "41", "41"
    FOURTY_TWO = "42", "42"
    FOURTY_THREE = "43", "43"
    FOURTY_FOUR = "44", "44"
    FOURTY_FIVE = "45", "45"
    FOURTY_SIX = "46", "46"
    FOURTY_SEVEN = "47", "47"


MERCH_SIZES = MiscSize.choices + ClothingSize.choices + ShoesSize.choices
