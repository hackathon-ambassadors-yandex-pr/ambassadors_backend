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

    NEW_PROFESSION = "Получение новой профессии, чтобы сменить работу", "New profession"
    DEEPEN_KNOWLEDGE = (
        "Углубление имеющихся знаний, чтобы использовать их в текущей работе",
        "Deepen knowledge",
    )
    OTHER = "Свой вариант", "Other"


class Gender(models.TextChoices):
    """Пол."""

    MALE = "М", "Male"
    FEMALE = "Ж", "Female"
