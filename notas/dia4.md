# Día 4 — Seguimiento, reporte y transacción segura

## 1. Seguimiento sin SQL en la plantilla

La ruta `GET /pedidos/<id>/` llega a `seguimiento_view`. La vista llama a
`obtener_datos_pedido`, en `services.py`, y recibe el pedido, su cobro y los
datos del mapa ya preparados. `seguimiento.html` sólo los presenta: no usa SQL
ni llama al ORM. El mapa es un recuadro ilustrativo con origen y destino y el
ETA se muestra desde el pedido guardado.

## 2. El mismo trámite sirve para el reporte

Tanto `seguimiento_view` como `reporte_pedido_view` llaman a
`obtener_datos_pedido`. Así la consulta y la preparación de datos no se copian.
El reporte está disponible en `GET /pedidos/<id>/reporte/`.

## 3. Pedido y cobro se guardan juntos

`registrar_pedido` abre `transaction.atomic()`. Dentro se crean el `Pedido` y
el `Cobro`. Si cualquiera de los dos falla, Django revierte ambos cambios y no
queda un pedido sin cobro.

## 4. El aviso externo espera al commit

`transaction.on_commit()` agenda `avisar_repartidor`. El aviso no se manda
dentro de la transacción: se ejecuta cuando Django ya confirmó correctamente
los datos. En esta demostración el aviso se escribe en la consola.

## 5. La consulta funciona aunque falle la IA

La IA simulada se usa sólo durante el alta para calcular el ETA. Si lanza una
excepción, se guarda `Por confirmar`. Después, el seguimiento lee directamente
la base local y no vuelve a llamar a la IA, por lo que `GET /pedidos/<id>/`
continúa respondiendo.

## Archivos principales

- `entregas/models.py`: modelos `Pedido` y `Cobro`.
- `entregas/services.py`: consulta compartida, transacción, fallback y aviso.
- `entregas/views.py`: vistas delgadas para alta, seguimiento y reporte.
- `entregas/templates/seguimiento.html`: mapa ilustrativo, ETA y cobro.
- `entregas/templates/reporte_pedido.html`: reporte que reutiliza el trámite.
- `entregas/tests.py`: pruebas de atomicidad, commit y falla de IA.
