"""Настройки БД приложения Sendings."""

from django.core.validators import MinValueValidator
from django.db import models

from apps.ambassadors.models import Address
from apps.sendings.choice_classes import MerchType, SendingStatus


class Merch(models.Model):
    """Параметры таблицы Merch."""

    name = models.CharField(
        "name",
        max_length=20,
        unique=True,
    )
    type = models.CharField(
        "type",
        max_length=20,
        choices=MerchType.choices,
    )
    unit_price = models.PositiveIntegerField(
        "unit price",
    )
    quantity = models.PositiveSmallIntegerField(
        "quantity",
    )

    class Meta:
        verbose_name = "merch"
        verbose_name_plural = "merch"

    def __str__(self):
        return self.name


class Sending(models.Model):
    """Параметры таблицы Sending."""

    reg_number = models.CharField(
        "registration number",
        editable=False,
    )
    address = models.ForeignKey(
        Address,
        verbose_name="address",
        on_delete=models.PROTECT,
        related_name="sendings",
    )
    created_at = models.DateTimeField(
        "date of creation",
        auto_now_add=True,
        db_index=True,
    )
    status = models.CharField(
        "status",
        max_length=20,
        choices=SendingStatus.choices,
        default=SendingStatus.SENT,
    )
    user_comment = models.TextField(
        "comment",
        blank=True,
    )
    merches = models.ManyToManyField(
        Merch,
        through="SendingToMerch",
        verbose_name="merch",
        related_name="sendings",
    )

    class Meta:
        verbose_name = "sending"
        verbose_name_plural = "sending"
        indexes = (models.Index(fields=("created_at",), name="created_at_idx"),)
        ordering = ("-created_at",)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.reg_number:
            self.reg_number = f"A {self.pk}"
            self.save()


class SendingToMerch(models.Model):
    """Параметры промежуточной таблицы для поля merches таблицы Sending."""

    sending = models.ForeignKey(
        Sending,
        verbose_name="sending",
        on_delete=models.PROTECT,
        related_name="sending_to_merches",
    )
    merch = models.ForeignKey(
        Merch,
        verbose_name="merch",
        on_delete=models.PROTECT,
        related_name="sending_to_merches",
    )
    size = models.CharField(
        "size",
        max_length=10,
    )
    quantity = models.PositiveIntegerField(
        "quantity",
        validators=(MinValueValidator(limit_value=1),),
    )
    unit_price = models.PositiveIntegerField(
        "unit price",
        help_text="Unit price at time of dispatch",
    )

    class Meta:
        verbose_name = "sending merch"
        verbose_name_plural = "sending merch"
        constraints = (
            models.UniqueConstraint(
                fields=("sending", "merch", "size"),
                name="merch_with_size_is_unique_in_sending",
                violation_error_message=(
                    "Merch with size must be unique in this sending."
                ),
            ),
        )

    def __str__(self):
        return f"Merch {self.merch.pk} in Sending {self.sending.pk}"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.unit_price = self.merch.unit_price
        super().save(*args, **kwargs)
