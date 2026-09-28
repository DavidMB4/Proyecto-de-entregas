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


class Cobro(models.Model):
    """Cobro simulado asociado a un solo pedido."""

    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name="cobro",
    )
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default="Aprobado")
    fecha_cobro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cobro de ${self.monto} para pedido #{self.pedido_id}"
