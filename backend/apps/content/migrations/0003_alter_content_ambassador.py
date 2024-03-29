# Generated by Django 4.2 on 2024-03-11 03:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ambassadors", "0001_initial"),
        ("content", "0002_alter_content_social_network"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="ambassador",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="contents",
                to="ambassadors.ambassador",
                verbose_name="ambassador",
            ),
        ),
    ]
