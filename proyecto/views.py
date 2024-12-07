from django.shortcuts import render
from django.conf import settings
from .models import Receta
from django.core.mail import send_mail

def busqueda_recetas(request):
    """Renderiza la página de búsqueda de recetas."""
    return render(request, "buscar.html")

def buscar(request):
    """Busca recetas en la base de datos y envía correos si se captura un mensaje."""
    mensaje = None
    recetas = None
    query_receta = request.GET.get("receta", "").strip()

    # Validación de búsqueda
    if query_receta:
        if len(query_receta) > 50:
            mensaje = 'El texto de búsqueda es demasiado largo, intenta nuevamente.'
        else:
            # Busca recetas por coincidencia en el nombre
            recetas = Receta.objects.filter(nombre__icontains=query_receta)
            if not recetas:
                mensaje = 'No se encontraron recetas que coincidan con la búsqueda.'
    else:
        mensaje = 'No ingresaste nada en el campo de búsqueda.'

    # Enviar correo si se captura un mensaje desde el formulario
    if request.method == 'POST':
        var_asunto = request.POST.get("asunto", "")
        var_mensaje = f"{request.POST.get('mensaje', '')}\n\nDe: {request.POST.get('email', '')}"
        var_email_from = settings.EMAIL_HOST_USER
        receptor = ["tu_correo@ejemplo.com"]  # Cambia a tu correo para recibir el mensaje

        # Envía el correo y redirige a la página de agradecimiento
        send_mail(var_asunto, var_mensaje, var_email_from, receptor)
        return render(request, "gracias.html")

    return render(request, "resultado.html", {"recetas": recetas, "query": query_receta, "mensaje": mensaje})

def gracias(request):
    """Renderiza la página de agradecimiento."""
    return render(request, "gracias.html")
