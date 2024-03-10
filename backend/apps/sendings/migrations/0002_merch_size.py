# Generated by Django 4.2 on 2024-03-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sendings", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="merch",
            name="size",
            field=models.CharField(
                choices=[
                    ("NZ", "No size"),
                    ("XS", "XS"),
                    ("S", "S"),
                    ("M", "M"),
                    ("L", "L"),
                    ("XL", "XL"),
                    ("34", "34"),
                    ("35", "35"),
                    ("36", "36"),
                    ("37", "37"),
                    ("38", "38"),
                    ("39", "39"),
                    ("40", "40"),
                    ("41", "41"),
                    ("42", "42"),
                    ("43", "43"),
                    ("44", "44"),
                    ("45", "45"),
                    ("46", "46"),
                    ("47", "47"),
                ],
                default="NZ",
                max_length=10,
                verbose_name="size",
            ),
        ),
    ]
