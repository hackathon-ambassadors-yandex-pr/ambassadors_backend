# Generated by Django 4.2 on 2024-03-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sendings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="merch",
            name="size",
            field=models.CharField(default="NZ", max_length=10, verbose_name="size"),
            preserve_default=False,
        ),
    ]
