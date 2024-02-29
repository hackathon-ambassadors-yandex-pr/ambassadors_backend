from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """Модель пользователя."""

    username = models.CharField(
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        default="",
        verbose_name="имя пользователя",
    )
    first_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name="имя",
    )
    middle_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name="отчество",
    )
    last_name = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name="фамилия",
    )
    email = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        unique=True,
        verbose_name="почта",
    )
    registration_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="дата регистрации",
    )
    avatar = models.ImageField(
        upload_to="user/avatars", blank=True, null=True, verbose_name="Фото"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ("last_name",)
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.username
