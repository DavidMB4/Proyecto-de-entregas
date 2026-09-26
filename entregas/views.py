from django.shortcuts import render, redirect, get_object_or_404
from . import services

def crear_pedido_view(request):
    #Este es el POST para enviar el formulario de un pedido
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

        #Redirige a la vista de seguimiento
        return redirect(f'/pedidos/{pedido.id}/')

    # Si es GET, le mostrmos e formulario en blanco
    return render(request, 'crear_pedido.html')


def seguimiento_view(request, id):
    # Muestra la pantalla de seguimiento de un pedido
    pedido = services.obtener_pedido(id)
    return render(request, 'seguimiento.html', {'pedido': pedido})