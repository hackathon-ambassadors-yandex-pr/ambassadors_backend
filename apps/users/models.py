from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    """Менеджер пользователей для создания и управления пользователями."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Введите email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя."""

    first_name = models.CharField(
        "first name",
        max_length=20,
    )
    middle_name = models.CharField(
        "middle name",
        max_length=20,
    )
    last_name = models.CharField(
        "last name",
        max_length=20,
    )
    email = models.EmailField(
        "email",
        unique=True,
    )
    registration_date = models.DateField(
        "registration date",
        auto_now_add=True,
    )
    avatar = models.ImageField(
        "avatar",
        upload_to="users/avatars",
        blank=True,
    )
    is_active = models.BooleanField(
        "active status",
        default=True,
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    class Meta:
        ordering = ("last_name",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
