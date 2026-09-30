from django.db import models


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
