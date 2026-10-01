"""
Created on 30/09/2026
Created by Daryna Bogaevska

Splits "university, country" into two separate fields using RunPython.
Rolling back joins them again with a comma.
"""
from django.db import migrations


def split_university_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        text = program.university.strip()
        if text.endswith(")") and "(" in text:
            name, country = text[:-1].rsplit("(", 1)
        elif "," in text:
            name, country = text.rsplit(",", 1)
        elif " - " in text:
            name, country = text.rsplit(" - ", 1)
        else:
            name, country = text, ""
        program.university = name.strip()
        program.country = country.strip()
        program.save(update_fields=["university", "country"])


def join_university_and_country(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.exclude(country=""):
        program.university = f"{program.university}, {program.country}"
        program.country = ""
        program.save(update_fields=["university", "country"])


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0003_exchangeprogram_country"),
    ]

    operations = [
        migrations.RunPython(
            split_university_and_country,
            reverse_code=join_university_and_country,
        ),
    ]
