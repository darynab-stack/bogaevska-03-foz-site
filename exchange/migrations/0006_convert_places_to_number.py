import re

from django.db import migrations


def text_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        match = re.search(r"\d+", program.places)
        if match is None:
            raise ValueError(f"No number in places for {program.university!r}")
        program.places_number = int(match.group())
        program.save(update_fields=["places_number"])


def number_to_text(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_number)
        program.save(update_fields=["places"])


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0005_exchangeprogram_places_number"),
    ]

    operations = [
        migrations.RunPython(text_to_number, reverse_code=number_to_text),
    ]
