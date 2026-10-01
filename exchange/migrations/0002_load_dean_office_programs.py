"""
Created on 30/09/2026
Created by Daryna Bogaevska

Loads the dean's office exchange programs as is, using RunSQL.
Rolling back deletes these programs.
"""
from django.db import migrations

LOAD_PROGRAMS_SQL = """
INSERT INTO exchange_exchangeprogram
    (university, languages, places, deadline, description)
VALUES
    ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
     'Найбільший університет Польщі, заснований 1816 року. Студенти обміну можуть обрати курси з психології, соціології та громадського здоров''я польською або англійською мовою.'),
    ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
     'Один із найстаріших університетів Європи (заснований 1425 року) із сильними програмами з медицини та психології. Навчання для студентів обміну проходить англійською.'),
    ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
     'Найстаріший університет Балтійських країн, заснований 1579 року. Пропонує англомовні курси з медицини, психології та соціальної роботи.'),
    ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
     'Найстаріший університет Польщі, заснований 1364 року. Його Collegium Medicum має окремий факультет наук про здоров''я.'),
    ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
     'Провідний університет Естонії, заснований 1632 року. Відомий дослідженнями в галузі психології та медицини.'),
    ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
     'Другий за розміром університет Чехії, розташований у Брно. Пропонує англомовні курси з психології, соціальної політики та соціальної роботи.');
"""

UNLOAD_PROGRAMS_SQL = """
DELETE FROM exchange_exchangeprogram
WHERE university LIKE 'Uniwersytet Warszawski%'
   OR university LIKE 'KU Leuven%'
   OR university LIKE 'Vilnius University%'
   OR university LIKE 'Uniwersytet Jagielloński%'
   OR university LIKE 'University of Tartu%'
   OR university LIKE 'Masaryk University%';
"""


class Migration(migrations.Migration):
    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(LOAD_PROGRAMS_SQL, reverse_sql=UNLOAD_PROGRAMS_SQL),
    ]
