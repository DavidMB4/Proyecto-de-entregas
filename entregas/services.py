from .models import Pedido

def registrar_pedido(origen, destino, peso_kg, distancia_km=10.0, urgente=False):
   # Crea y guarda un pedido en la base de datos.
    
    pedido = Pedido.objects.create(
        origen=origen,
        destino=destino,
        peso_kg=peso_kg,
        distancia_km=distancia_km,
        urgente=urgente,
        estado='Registrado',
        eta='2 dias' if not urgente else '1 dia'
    )
    return pedido

def obtener_pedido(pedido_id):
    # Busca un pedido por su ID/Folio.
    return Pedido.objects.get(id=pedido_id)