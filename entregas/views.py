from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . import services

def crear_pedido_view(request):
    # Este es el POST para enviar el formulario de un pedido
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

        # Redirige a la vista de seguimiento (PRG)
        return redirect(f'/pedidos/{pedido.id}/')

    # Si es GET, mostramos el formulario
    return render(request, 'crear_pedido.html')


def seguimiento_view(request, id):
    # Muestra la pantalla de seguimiento de un pedido
    pedido = services.obtener_pedido(id)
    return render(request, 'seguimiento.html', {'pedido': pedido})


def estado(request):
    # Vista para verificiacion del estado del sistema (Para la actividad extra del Lunes 5)
    return JsonResponse({
        "servicio": "entregas",
        "version": 1,
        "medios_disponibles": ["camioneta", "moto", "bicicleta", "dron"],
    })