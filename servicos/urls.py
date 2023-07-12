from django.urls import path

from . import views

app_name = "servicos"

urlpatterns = [
    path("", views.index, name="index"),
    path("servicos/", views.servicos, name="servicos"),
]