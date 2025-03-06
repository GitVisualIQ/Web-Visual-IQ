from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("visualiq/", views.visualiq, name="visualiq"),
    path("nuestro-servicio/", views.nuestro_servicio, name="nuestro-servicio"),
    path("equipo/", views.equipo, name="equipo"),
    path("contacto/", views.contacto, name="contacto"),
]