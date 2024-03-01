# Generated by Django 4.2 on 2024-03-01 13:34

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
                ("first_name", models.CharField(max_length=20, verbose_name="имя")),
                (
                    "middle_name",
                    models.CharField(max_length=20, verbose_name="отчество"),
                ),
                ("last_name", models.CharField(max_length=20, verbose_name="фамилия")),
                (
                    "gender",
                    models.CharField(
                        choices=[("М", "Male"), ("Ж", "Female")],
                        max_length=5,
                        verbose_name="пол",
                    ),
                ),
                (
                    "registration_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="дата регистрации"
                    ),
                ),
                (
                    "user_comment",
                    models.TextField(
                        blank=True, null=True, verbose_name="комментарий пользователя"
                    ),
                ),
                (
                    "clothing_size",
                    models.CharField(
                        choices=[
                            ("XS", "Extra Small"),
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                            ("XL", "Extra Large"),
                        ],
                        max_length=5,
                        verbose_name="размер одежды",
                    ),
                ),
                (
                    "shoe_size",
                    models.CharField(max_length=5, verbose_name="размер обуви"),
                ),
                (
                    "telegram_login",
                    models.CharField(
                        max_length=20, verbose_name="имя пользователя телеграм"
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                (
                    "mobile_phone",
                    models.CharField(max_length=20, verbose_name="номер телефона"),
                ),
                ("blog_link", models.URLField(verbose_name="ссылка на блог")),
                ("education", models.TextField(verbose_name="образование")),
                ("work_place", models.TextField(verbose_name="место работы")),
                (
                    "education_target",
                    models.TextField(
                        choices=[
                            (
                                "NEW_PROFESSION",
                                "получение новой профессии, чтобы сменить работу",
                            ),
                            (
                                "DEEPEN_KNOWLEDGE",
                                "углубление имеющихся знаний, чтобы использовать их в текущей работе",
                            ),
                            ("OTHER", "свой вариант"),
                        ],
                        verbose_name="цель образования",
                    ),
                ),
                (
                    "education_target_own",
                    models.TextField(
                        blank=True, null=True, verbose_name="своя цель образования"
                    ),
                ),
                (
                    "onboarding_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата онбординга"
                    ),
                ),
                (
                    "guide_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата прохождения гайда"
                    ),
                ),
                (
                    "comment_ambassador",
                    models.TextField(
                        blank=True, null=True, verbose_name="комментарий амбассадора"
                    ),
                ),
            ],
            options={
                "verbose_name": "амбассадор",
                "verbose_name_plural": "амбассадоры",
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
                    models.CharField(
                        max_length=30, unique=True, verbose_name="название программы"
                    ),
                ),
            ],
            options={
                "verbose_name": "программа",
                "verbose_name_plural": "программы",
            },
        ),
        migrations.CreateModel(
            name="Status",
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
                    models.CharField(
                        max_length=20, unique=True, verbose_name="название статуса"
                    ),
                ),
            ],
            options={
                "verbose_name": "статус",
                "verbose_name_plural": "статусы",
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
                (
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="название цели"
                    ),
                ),
            ],
            options={
                "verbose_name": "цель",
                "verbose_name_plural": "цели",
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
                    models.CharField(max_length=20, verbose_name="значение промокода"),
                ),
                (
                    "replaced_at",
                    models.DateField(blank=True, null=True, verbose_name="дата замены"),
                ),
                (
                    "is_current",
                    models.BooleanField(default=True, verbose_name="текущий"),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="promocodes",
                        to="ambassadors.ambassador",
                        verbose_name="амбассадор",
                    ),
                ),
            ],
            options={
                "verbose_name": "промокод",
                "verbose_name_plural": "промокоды",
            },
        ),
        migrations.AddField(
            model_name="ambassador",
            name="program",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="ambassadors.program",
                verbose_name="программа",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassadors",
                to="ambassadors.status",
                verbose_name="статус",
            ),
        ),
        migrations.AddField(
            model_name="ambassador",
            name="targets",
            field=models.ManyToManyField(
                related_name="ambassadors", to="ambassadors.target"
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
                ("country", models.CharField(max_length=20, verbose_name="страна")),
                ("city", models.CharField(max_length=20, verbose_name="город")),
                ("address", models.CharField(max_length=50, verbose_name="адрес")),
                (
                    "code",
                    models.CharField(max_length=10, verbose_name="почтовый индекс"),
                ),
                (
                    "replaced_at",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата изменения"
                    ),
                ),
                (
                    "is_current",
                    models.BooleanField(default=True, verbose_name="текущий"),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="ambassadors.ambassador",
                        verbose_name="амбассадор",
                    ),
                ),
            ],
            options={
                "verbose_name": "адрес",
                "verbose_name_plural": "адреса",
            },
        ),
    ]
