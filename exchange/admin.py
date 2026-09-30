from django.contrib import admin

from .models import ExchangeProgram


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ["university", "country", "languages", "places", "deadline"]
    list_filter = ["country"]
    search_fields = ["university", "country"]
