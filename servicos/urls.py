from django.urls import path

from . import views

app_name = "servicos"

urlpatterns = [
    path("", views.servicos, name="servicos"),
]