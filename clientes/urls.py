from django.urls import path
from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastro, name="cadastro"),
    ]