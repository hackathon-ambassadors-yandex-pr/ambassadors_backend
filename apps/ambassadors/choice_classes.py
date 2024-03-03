from django.db import models


class ClothingSize(models.TextChoices):
    """Размеры одежды."""

    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"


class EducationTarget(models.TextChoices):
    """Цели обучения."""

    NEW_PROFESSION = "New profession", "Получение новой профессии, чтобы сменить работу"
    DEEPEN_KNOWLEDGE = (
        "Deepen knowledge",
        "Углубление имеющихся знаний, чтобы использовать их в текущей работе",
    )
    OTHER = "Other", "Свой вариант"


class Gender(models.TextChoices):
    """Пол."""

    MALE = "Male", "М"
    FEMALE = "Female", "Ж"
