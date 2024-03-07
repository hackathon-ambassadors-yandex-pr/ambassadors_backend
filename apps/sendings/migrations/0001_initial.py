# Generated by Django 4.2 on 2024-03-07 12:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ambassadors", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Merch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=20, unique=True, verbose_name="name"),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Обувь", "Shoes"),
                            ("Одежда", "Clothing"),
                            ("Разное", "Misc"),
                        ],
                        max_length=20,
                        verbose_name="type",
                    ),
                ),
                ("unit_price", models.PositiveIntegerField(verbose_name="unit price")),
                (
                    "quantity",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1)
                        ],
                        verbose_name="quantity",
                    ),
                ),
            ],
            options={
                "verbose_name": "merch",
                "verbose_name_plural": "merch",
            },
        ),
        migrations.CreateModel(
            name="Sending",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reg_number",
                    models.CharField(
                        editable=False, verbose_name="registration number"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="date of creation",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Отправлено", "Sent"), ("Ошибка", "Error")],
                        default="Отправлено",
                        max_length=20,
                        verbose_name="status",
                    ),
                ),
                ("user_comment", models.TextField(blank=True, verbose_name="comment")),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sendings",
                        to="ambassadors.address",
                        verbose_name="address",
                    ),
                ),
            ],
            options={
                "verbose_name": "sending",
                "verbose_name_plural": "sending",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="SendingToMerch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("size", models.CharField(max_length=10, verbose_name="size")),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1)
                        ],
                        verbose_name="quantity",
                    ),
                ),
                (
                    "unit_price",
                    models.PositiveIntegerField(
                        help_text="Unit price at time of dispatch",
                        verbose_name="unit price",
                    ),
                ),
                (
                    "merch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sending_to_merches",
                        to="sendings.merch",
                        verbose_name="merch",
                    ),
                ),
                (
                    "sending",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sending_to_merches",
                        to="sendings.sending",
                        verbose_name="sending",
                    ),
                ),
            ],
            options={
                "verbose_name": "sending merch",
                "verbose_name_plural": "sending merch",
            },
        ),
        migrations.AddField(
            model_name="sending",
            name="merches",
            field=models.ManyToManyField(
                related_name="sendings",
                through="sendings.SendingToMerch",
                to="sendings.merch",
                verbose_name="merch",
            ),
        ),
        migrations.AddConstraint(
            model_name="sendingtomerch",
            constraint=models.UniqueConstraint(
                fields=("sending", "merch", "size"),
                name="merch_with_size_is_unique_in_sending",
                violation_error_message="Merch with size must be unique in this sending.",
            ),
        ),
        migrations.AddIndex(
            model_name="sending",
            index=models.Index(fields=["created_at"], name="created_at_idx"),
        ),
    ]
