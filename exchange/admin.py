from django.contrib import admin

from .models import ExchangeProgram


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = [
        "university",
        "country",
        "languages",
        "places",
        "deadline",
        "is_open",
    ]
    list_filter = ["country"]
    search_fields = ["university", "country"]

    @admin.display(boolean=True, description="Прийом триває")
    def is_open(self, obj):
        return obj.is_open
