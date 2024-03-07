# Generated by Django 4.2 on 2024-03-07 21:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ambassador",
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
                    "first_name",
                    models.CharField(max_length=20, verbose_name="first name"),
                ),
                (
                    "middle_name",
                    models.CharField(max_length=20, verbose_name="middle name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=20, verbose_name="last name"),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("М", "Male"), ("Ж", "Female")],
                        max_length=6,
                        verbose_name="gender",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Новый", "New"),
                            ("Активный", "Active"),
                            ("Уточняется", "TBC"),
                            ("На паузе", "On Pause"),
                            ("Архив", "Archive"),
                        ],
                        default="Новый",
                        max_length=20,
                        verbose_name="status",
                    ),
                ),
                (
                    "registration_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="registration date"
                    ),
                ),
                ("user_comment", models.TextField(blank=True, verbose_name="comment")),
                (
                    "clothing_size",
                    models.CharField(
                        choices=[
                            ("XS", "XS"),
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("XL", "XL"),
                        ],
                        max_length=5,
                        verbose_name="clothing size",
                    ),
                ),
                ("shoe_size", models.CharField(max_length=5, verbose_name="shoe size")),
                (
                    "telegram_link",
                    models.URLField(
                        max_length=50, unique=True, verbose_name="telegram link"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email"
                    ),
                ),
                (
                    "mobile_phone",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="mobile phone"
                    ),
                ),
                ("blog_link", models.URLField(unique=True, verbose_name="blog link")),
                ("education", models.TextField(verbose_name="education")),
                ("work_place", models.TextField(verbose_name="work place")),
                (
                    "education_target",
                    models.TextField(
                        choices=[
                            (
                                "Получение новой профессии, чтобы сменить работу",
                                "New Profession",
                            ),
                            (
                                "Углубление имеющихся знаний, чтобы использовать их в текущей работе",
                                "Deepen Knowledge",
                            ),
                            ("Свой вариант", "Other"),
                        ],
                        verbose_name="education target",
                    ),
                ),
                (
                    "education_target_own",
                    models.TextField(
                        blank=True, verbose_name="own target of education"
                    ),
                ),
                (
                    "onboarding_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="onboarding date"
                    ),
                ),
                (
                    "guide_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="date of completion of guide",
                    ),
                ),
                (
                    "comment_ambassador",
                    models.TextField(blank=True, verbose_name="ambassador's comment"),
                ),
            ],
            options={
                "verbose_name": "ambassador",
                "verbose_name_plural": "ambassadors",
            },
        ),
        migrations.CreateModel(
            name="Program",
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
                    models.CharField(max_length=50, unique=True, verbose_name="name"),
                ),
            ],
            options={
                "verbose_name": "program",
                "verbose_name_plural": "programs",
            },
        ),
        migrations.CreateModel(
            name="Target",
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
                ("name", models.TextField(unique=True, verbose_name="name")),
            ],
            options={
                "verbose_name": "target",
                "verbose_name_plural": "targets",
            },
        ),
        migrations.CreateModel(
            name="Promocode",
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
                    "value",
                    models.CharField(max_length=20, verbose_name="promocode value"),
                ),
                (
                    "replaced_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="replacement date"
                    ),
                ),
                (
                    "is_current",
                    models.BooleanField(default=True, verbose_name="current"),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="promocodes",
                        to="ambassadors.ambassador",
                        verbose_name="ambassador",
                    ),
                ),
            ],
            options={
                "verbose_name": "promocode",
                "verbose_name_plural": "promocodes",
            },
        ),
        migrations.AddField(
            model_name="ambassador",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="ambassadors.program",
                verbose_name="program",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="targets",
            field=models.ManyToManyField(
                related_name="ambassadors",
                to="ambassadors.target",
                verbose_name="targets",
            ),
        ),
        migrations.CreateModel(
            name="Address",
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
                ("country", models.CharField(max_length=20, verbose_name="country")),
                ("city", models.CharField(max_length=20, verbose_name="city")),
                ("address", models.CharField(max_length=100, verbose_name="address")),
                ("code", models.CharField(max_length=10, verbose_name="postal code")),
                (
                    "replaced_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="replacement date"
                    ),
                ),
                (
                    "is_current",
                    models.BooleanField(default=True, verbose_name="current"),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="ambassadors.ambassador",
                        verbose_name="ambassador",
                    ),
                ),
            ],
            options={
                "verbose_name": "address",
                "verbose_name_plural": "addresses",
            },
        ),
        migrations.AddConstraint(
            model_name="ambassador",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("education_target", "Свой вариант"),
                        models.Q(("education_target_own", ""), _negated=True),
                    ),
                    models.Q(
                        models.Q(("education_target", "Свой вариант"), _negated=True),
                        ("education_target_own", ""),
                    ),
                    _connector="OR",
                ),
                name="education_target_and_education_target_own",
                violation_error_message="if education_target = OTHER, then education_target_own field cannot be empty, and vice versa.",
            ),
        ),
    ]
