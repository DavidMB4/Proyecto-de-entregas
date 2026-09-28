from django.http import Http404
from django.shortcuts import redirect, render

from . import services
from .models import Pedido


def crear_pedido_view(request):
    # Este es el POST para enviar el formulario de un pedido.
    if request.method == 'POST':
        origen = request.POST.get('origen', '')
        destino = request.POST.get('destino', '')
        peso_kg = float(request.POST.get('peso_kg', 1.0))
        urgente = request.POST.get('urgente') == 'on'

        pedido = services.registrar_pedido(
            origen=origen,
            destino=destino,
            peso_kg=peso_kg,
            urgente=urgente
        )

        # Patrón PRG: evita repetir el alta si se actualiza la página.
        return redirect('seguimiento', id=pedido.id)

    # Si es GET, mostramos el formulario en blanco.
    return render(request, 'crear_pedido.html')


def seguimiento_view(request, id):
    try:
        datos = services.obtener_datos_pedido(id)
    except Pedido.DoesNotExist as error:
        raise Http404("El pedido no existe") from error
    return render(request, 'seguimiento.html', datos)


def reporte_pedido_view(request, id):
    """Reutiliza exactamente el mismo trámite que el seguimiento."""
    try:
        datos = services.obtener_datos_pedido(id)
    except Pedido.DoesNotExist as error:
        raise Http404("El pedido no existe") from error
    return render(request, 'reporte_pedido.html', datos)
