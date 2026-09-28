import logging
from decimal import Decimal

from django.db import transaction

from .models import Cobro, Pedido


logger = logging.getLogger(__name__)


def calcular_eta_con_ia(origen, destino, urgente=False):
    """Simula al proveedor de IA que calcula el tiempo de entrega.

    En un proyecto real, la llamada HTTP al proveedor externo viviría aquí,
    nunca en la plantilla ni en la vista.
    """
    return "1 día" if urgente else "2 días"


def avisar_repartidor(pedido_id):
    """Simula un aviso externo; por ahora queda visible en la consola."""
    logger.info("Aviso enviado al repartidor para el pedido %s", pedido_id)


def calcular_monto(peso_kg, urgente=False):
    """Calcula un cobro de demostración sin usar dinero de tipo float."""
    monto = Decimal("50.00") + (Decimal(str(peso_kg)) * Decimal("12.00"))
    if urgente:
        monto += Decimal("35.00")
    return monto.quantize(Decimal("0.01"))


def registrar_pedido(origen, destino, peso_kg, distancia_km=10.0, urgente=False):
    """Crea el pedido y su cobro como una sola operación atómica."""
    try:
        eta = calcular_eta_con_ia(origen, destino, urgente)
    except Exception:
        # La falla de un proveedor externo no impide guardar el pedido.
        logger.exception("La IA no respondió; se usará un ETA de respaldo")
        eta = "Por confirmar"

    with transaction.atomic():
        pedido = Pedido.objects.create(
            origen=origen,
            destino=destino,
            peso_kg=peso_kg,
            distancia_km=distancia_km,
            urgente=urgente,
            estado="Registrado",
            eta=eta,
        )
        Cobro.objects.create(
            pedido=pedido,
            monto=calcular_monto(peso_kg, urgente),
            estado="Aprobado",
        )

        # El aviso se ejecuta sólo después de confirmar la transacción.
        transaction.on_commit(lambda: avisar_repartidor(pedido.id))

    return pedido


def obtener_datos_pedido(pedido_id):
    """Trámite de consulta compartido por seguimiento y reporte."""
    pedido = Pedido.objects.select_related("cobro").get(id=pedido_id)
    return {
        "pedido": pedido,
        "cobro": pedido.cobro,
        "mapa": {
            "origen": pedido.origen,
            "destino": pedido.destino,
            "descripcion": f"Ruta de {pedido.origen} a {pedido.destino}",
        },
    }


def obtener_pedido(pedido_id):
    """Se conserva para no romper el código previo de los días 1 y 2."""
    return Pedido.objects.get(id=pedido_id)
