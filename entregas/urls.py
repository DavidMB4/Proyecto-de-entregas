from django.urls import path
from . import views

urlpatterns = [
    # Ruta de verificación del estado del sistema en JSON para la Actividad extra de la clase del lunes 5
    path("estado/", views.estado, name="estado"),

    # Rutas para crear pedidos y seguimiento
    path("pedidos/", views.crear_pedido_view, name="crear_pedido"),
    path("pedidos/<int:id>/", views.seguimiento_view, name="seguimiento"),
]