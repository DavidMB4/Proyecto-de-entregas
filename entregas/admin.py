from django.contrib import admin

from .models import Cobro, Pedido


admin.site.register(Pedido)
admin.site.register(Cobro)
