from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
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
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')
        # Enviar correo con los datos del formulario
        send_mail(
            subject=f'Nuevo mensaje de {nombre} desde la web de Visual IQ',
            message=f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\n\n\nMensaje: {mensaje}',
            from_email='tuemail@example.com',  # Configura tu email en settings.py
            recipient_list=['pvallasciani@visualiq.tech'],  # Cambia por tu email
            fail_silently=False,
        )
        return HttpResponse("Mensaje enviado con éxito")
    return render(request, 'contacto.html')