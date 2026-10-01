"""
Created on 30/09/2026
Created by Daryna Bogaevska

Views that load faculty data from the database and render the home,
study program and department pages.
"""

from django.shortcuts import get_object_or_404, render

from .models import Department, FacultyInfo, Program, Teacher


def home(request):
    context = {
        "faculty": FacultyInfo.objects.first(),
        "department_count": Department.objects.count(),
        "program_count": Program.objects.count(),
        "teacher_count": Teacher.objects.count(),
    }
    return render(request, "faculty/home.html", context)


def program_list(request):
    programs = Program.objects.select_related("department")
    return render(request, "faculty/program_list.html", {"programs": programs})


def program_detail(request, pk):
    program = get_object_or_404(Program.objects.select_related("department"), pk=pk)
    return render(request, "faculty/program_detail.html", {"program": program})


def department_list(request):
    departments = Department.objects.prefetch_related("programs")
    return render(request, "faculty/department_list.html", {"departments": departments})


def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, "faculty/department_detail.html", {"department": department})
