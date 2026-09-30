from django.shortcuts import get_object_or_404, render

from .models import Department, FacultyInfo, Program


def home(request):
    faculty = FacultyInfo.objects.first()
    return render(request, "faculty/home.html", {"faculty": faculty})


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
