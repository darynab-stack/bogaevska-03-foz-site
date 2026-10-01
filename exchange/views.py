from django.shortcuts import render

from .models import ExchangeProgram


def program_list(request):
    programs = ExchangeProgram.objects.all()
    countries = programs.order_by("country").values_list("country", flat=True)
    selected_country = request.GET.get("country", "")
    if selected_country:
        programs = programs.filter(country=selected_country)
    context = {
        "programs": programs,
        "countries": countries.distinct(),
        "selected_country": selected_country,
    }
    return render(request, "exchange/program_list.html", context)
