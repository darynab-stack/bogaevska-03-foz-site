"""
Created on 30/09/2026
Created by Daryna Bogaevska

URL route for the exchange programs page.
"""

from django.urls import path

from . import views

app_name = "exchange"

urlpatterns = [
    path("", views.program_list, name="program_list"),
]
