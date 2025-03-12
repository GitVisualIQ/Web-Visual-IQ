from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def main(request):
    return render(request, 'main.html')

def visualiq(request):
    return render(request, 'visualiq.html')

def nuestro_servicio(request):
    return render(request, 'nuestro_servicio.html')

def equipo(request):
    return render(request, 'equipo.html')

def contacto(request):
    return render(request, 'contacto.html')