from django.db import models


class FacultyInfo(models.Model):
    name = models.CharField("назва факультету", max_length=200)
    description = models.TextField("опис факультету")
    dean = models.CharField("декан", max_length=200)
    address = models.CharField("адреса", max_length=300)
    phone = models.CharField("телефон", max_length=50)
    email = models.EmailField("електронна пошта", blank=True)

    class Meta:
        verbose_name = "інформація про факультет"
        verbose_name_plural = "інформація про факультет"

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField("назва", max_length=200)
    head = models.CharField("завідувач кафедри", max_length=200)

    class Meta:
        verbose_name = "кафедра"
        verbose_name_plural = "кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("назва", max_length=200)
    code = models.CharField("код", max_length=20)
    description = models.TextField("опис")
    coordinator_name = models.CharField("координатор набору", max_length=200)
    coordinator_contact = models.CharField("контакт координатора", max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="programs",
        verbose_name="випускова кафедра",
    )
    disciplines = models.TextField(
        "список дисциплін",
        blank=True,
        help_text="Кожна дисципліна з нового рядка.",
    )

    class Meta:
        verbose_name = "спеціальність"
        verbose_name_plural = "спеціальності"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} {self.name}"

    def disciplines_list(self):
        return [line.strip() for line in self.disciplines.splitlines() if line.strip()]


class Teacher(models.Model):
    name = models.CharField("ім'я", max_length=200)
    position = models.CharField("посада", max_length=200)
    degree = models.CharField("науковий ступінь", max_length=200, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="teachers",
        verbose_name="кафедра",
    )

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"
        ordering = ["name"]

    def __str__(self):
        return self.name

