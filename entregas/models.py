from django.db import models

class Pedido(models.Model):
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    peso_kg = models.FloatField(default=1.0)
    distancia_km = models.FloatField(default=10.0)
    urgente = models.BooleanField(default=False)
    estado = models.CharField(max_length=50, default='Registrado')
    eta = models.CharField(max_length=50, default='Pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Pedido #{self.id}: {self.origen} ➔ {self.destino}"