from django.db import models

from apps.ambassadors.models import Ambassador
from apps.content.choice_classes import ContentStatus


class SocialNetwork(models.Model):
    """Таблица SocialNetwork."""

    name = models.CharField(
        "name",
        max_length=30,
        unique=True,
    )

    class Meta:
        verbose_name = "social network"
        verbose_name_plural = "social networks"

    def __str__(self):
        return f"Social network {self.name}"


class Content(models.Model):
    """Таблица Content."""

    ambassador = models.ForeignKey(
        Ambassador,
        on_delete=models.PROTECT,
        null=True,
        verbose_name="ambassador",
        related_name="contents",
    )
    incorrect_first_name = models.CharField(
        "incorrect first name",
        max_length=20,
        blank=True,
        help_text="Incorrect first name from form",
    )
    incorrect_last_name = models.CharField(
        "incorrect last name",
        max_length=20,
        blank=True,
        help_text="Incorrect last name from form",
    )
    incorrect_telegram_link = models.CharField(
        "incorrect telegram link",
        max_length=50,
        blank=True,
        help_text="Incorrect telegram link from form",
    )
    link = models.URLField(
        "link",
        help_text="Link to content",
    )
    guide_check = models.BooleanField(
        "guide check",
        default=False,
        help_text="Content on topic of Beginner's Ambassador Guide",
    )
    status = models.CharField(
        "status",
        max_length=20,
        choices=ContentStatus.choices,
        default=ContentStatus.NEW,
    )
    uploaded_at = models.DateTimeField(
        "upload date",
        auto_now_add=True,
    )
    user_comment = models.TextField(
        "comment",
        blank=True,
    )
    social_network = models.ForeignKey(
        SocialNetwork,
        on_delete=models.PROTECT,
        verbose_name="social_network",
        related_name="contents",
    )

    class Meta:
        verbose_name = "content"
        verbose_name_plural = "content"
        constraints = (
            models.CheckConstraint(
                check=(
                    (
                        models.Q(ambassador__isnull=True)
                        & ~models.Q(incorrect_first_name="")
                        & ~models.Q(incorrect_last_name="")
                        & ~models.Q(incorrect_telegram_link="")
                    )
                    | (
                        models.Q(ambassador__isnull=False)
                        & models.Q(incorrect_first_name="")
                        & models.Q(incorrect_last_name="")
                        & models.Q(incorrect_telegram_link="")
                    )
                ),
                name="fields_for_incorrect_data_and_ambassador_field",
                violation_error_message=(
                    "Fields for incorrect data and ambassador field "
                    "cannot be empty or filled at same time."
                ),
            ),
        )

    def __str__(self):
        return f"Content № {self.id}"


class ContentFile(models.Model):
    """Таблица ContentFile."""

    content = models.ForeignKey(
        Content,
        on_delete=models.PROTECT,
        verbose_name="content",
        related_name="content_files",
    )
    file = models.FileField(
        "file",
        upload_to="content_files/",
        max_length=255,
    )

    class Meta:
        verbose_name = "content file"
        verbose_name_plural = "content files"

    def __str__(self):
        return f"Content file № {self.id}"
