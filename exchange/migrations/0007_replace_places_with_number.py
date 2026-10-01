"""
Created on 30/09/2026
Created by Daryna Bogaevska

Removes the old text field for the number of places
and renames the numeric field to places.
"""
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0006_convert_places_to_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="places",
        ),
        migrations.RenameField(
            model_name="exchangeprogram",
            old_name="places_number",
            new_name="places",
        ),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.PositiveSmallIntegerField(verbose_name="кількість місць"),
        ),
    ]
