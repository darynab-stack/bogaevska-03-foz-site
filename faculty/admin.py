"""
Created on 29/09/2026
Created by Daryna Bogaevska

Admin panel settings for the faculty models: list columns, filters and search.
Teachers can be added directly on the department page.
"""

from django.contrib import admin

from .models import Department, FacultyInfo, Program, Teacher


@admin.register(FacultyInfo)
class FacultyInfoAdmin(admin.ModelAdmin):
    list_display = ["name", "dean", "phone"]

    def has_add_permission(self, request):
        return not FacultyInfo.objects.exists()


class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]
    search_fields = ["name", "head"]
    inlines = [TeacherInline]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "department", "coordinator_name"]
    list_filter = ["department"]
    search_fields = ["name", "code"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "degree", "department"]
    list_filter = ["department"]
    search_fields = ["name"]
