"""
Created on 30/09/2026
Created by Daryna Bogaevska

Exchange program model. The admission status is calculated from the deadline
instead of being stored in the database.
"""

from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField("університет", max_length=200)
    country = models.CharField("країна", max_length=100, default="")
    languages = models.CharField("мови навчання", max_length=200)
    places = models.PositiveSmallIntegerField("кількість місць")
    deadline = models.DateField("дедлайн подачі")
    description = models.TextField("опис")

    class Meta:
        verbose_name = "програма обміну"
        verbose_name_plural = "програми обміну"
        ordering = ["deadline"]

    def __str__(self):
        return self.university

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()

    @property
    def status(self):
        return "Прийом триває" if self.is_open else "Прийом завершено"
