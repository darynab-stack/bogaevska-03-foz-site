"""
Created on 30/09/2026
Created by Daryna Bogaevska

Makes language names consistent ("English" -> "англійська").
Rolling back restores the original values of the dean's office programs.
"""
from django.db import migrations

LANGUAGE_NAMES = {
    "english": "англійська",
}

ORIGINAL_LANGUAGES = {
    "KU Leuven": "English",
    "Uniwersytet Jagielloński": "Польська, Англійська",
}


def normalize(text):
    languages = []
    for part in text.split(","):
        language = part.strip().lower()
        languages.append(LANGUAGE_NAMES.get(language, language))
    return ", ".join(languages)


def normalize_languages(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.languages = normalize(program.languages)
        program.save(update_fields=["languages"])


def restore_original_languages(apps, schema_editor):
    ExchangeProgram = apps.get_model("exchange", "ExchangeProgram")
    for university, languages in ORIGINAL_LANGUAGES.items():
        ExchangeProgram.objects.filter(university=university).update(
            languages=languages
        )


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0007_replace_places_with_number"),
    ]

    operations = [
        migrations.RunPython(
            normalize_languages,
            reverse_code=restore_original_languages,
        ),
    ]
