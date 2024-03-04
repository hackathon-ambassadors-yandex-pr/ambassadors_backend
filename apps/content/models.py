from django.db import models

from apps.content.choice_classes import ContentStatus
from apps.ambassadors.models import Ambassador


class SocialNetwork(models.Model):
    """Таблица SocialNetwork."""

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name="название социальной сети",
    )
    class Meta:
        verbose_name = "социальная сеть"
        verbose_name_plural = "социальные сети"

    def __str__(self):
        return f'социальная сеть {self.name}'
    
    
class Content(models.Model):
    """Таблица Content."""
    
    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.PROTECT,
        null=True,
        related_name="contents",
    )
    first_and_last_name = models.CharField(
        max_length=50,
        blank = True,
    )
    telegram_link = models.CharField(
        max_length=50,
        blank = True,
    )
    link = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    guide_check = models.BooleanField(
        default=False
    )
    status = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="статус",
        choices=ContentStatus.choices,
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="дата",
    )
    user_comment = models.TextField(
        verbose_name="комментарий",
    )
    social_network = models.ForeignKey(
        SocialNetwork,
        on_delete=models.PROTECT,
        related_name="contents",
    )

    class Meta:
        verbose_name = "контент"
        verbose_name_plural = "контент"

    def __str__(self):
        return f'Контент {self.first_and_last_name}'

class ContentFile(models.Model):
    """Таблица ContentFile."""

    ambassador = models.ForeignKey(
        Content,
        on_delete=models.PROTECT,
        null=True,
        related_name="content_files",
    )
    file = models.FileField(
        null=False,
        blank=False,
        verbose_name="путь до файла",
    )

    class Meta:
        verbose_name = "файл"
        verbose_name_plural = "файлы"

    def __str__(self):
        return f'Файл {self.file}'
