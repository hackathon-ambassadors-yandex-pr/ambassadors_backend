from django.db import models


class ClothingSize(models.TextChoices):
    """Размеры одежды."""

    XS = "XS", "XS"
    S = "S", "S"
    M = "M", "M"
    L = "L", "L"
    XL = "XL", "XL"


class EducationTarget(models.TextChoices):
    """Цели обучения."""

    NEW_PROFESSION = "Получение новой профессии, чтобы сменить работу"
    DEEPEN_KNOWLEDGE = (
        "Углубление имеющихся знаний, чтобы использовать их в текущей работе",
    )
    OTHER = "Свой вариант"


class Gender(models.TextChoices):
    """Пол."""

    MALE = "М"
    FEMALE = "Ж"


class AmbassadorStatus(models.TextChoices):
    """Статус амбассадора."""

    NEW = "Новый"
    ACTIVE = "Активный"
    TBC = "Уточняется", "TBC"
    ON_PAUSE = "На паузе"
    ARCHIVE = "Архив"
