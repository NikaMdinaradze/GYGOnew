# Generated by Django 4.2.7 on 2024-01-03 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("image", models.ImageField(upload_to="")),
                ("company", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Text",
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
                ("text", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("product", "Product"),
                            ("search", "Search"),
                            ("home", "Home"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
