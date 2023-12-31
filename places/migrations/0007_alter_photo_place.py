# Generated by Django 4.2.7 on 2023-12-22 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0006_alter_place_id_alter_place_number"),
    ]

    operations = [
        migrations.AlterField(

            model_name="photo",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="places.place",
            ),
        ),
    ]
