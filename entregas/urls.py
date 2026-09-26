from django.urls import path
from . import views

urlpatterns = [
    # Esta es la ruta para crear el pedido y ver el formulario:
    path('pedidos/', views.crear_pedido_view, name='crear_pedido'),
    
    # Esta ruta sirve para ver el seguimiento de un pedido por su id
    path('pedidos/<int:id>/', views.seguimiento_view, name='seguimiento'),
]