# Día 2 — Pensar el primer corte y arrancar Django

## Camino de la petición POST /pedidos

El flujo de procesamiento cuando un cliente envía un formulario para crear un pedido (`POST /pedidos`) en la aplicación Django recorre estas partes:

1. **Cliente / Navegador:**  
   Envía la petición HTTP con método `POST` y los datos del formulario (`origen`, `destino`, `peso_kg`, `urgente`) hacia `/pedidos/`.

2. **Cadena de Middlewares en `settings.py`:**  
   Django ya instancia su propia Chain of Responsibility de forma automatica.
   La petición atraviesa los middlewares nativos de Django (`SecurityMiddleware`, `SessionMiddleware`, `CsrfViewMiddleware`, `AuthenticationMiddleware`) para validar seguridad y tokens CSRF.

3. **Front Controller / Tabla de Enrutamiento con `config/urls.py` y `entregas/urls.py`:**  
   El enrutador central de Django recibe la URL `/pedidos/` y despacha la ejecución hacia la vista correspondiente (`crear_pedido_view`).

4. **Page Controller / Vista delgada (`entregas/views.py` ➔ `crear_pedido_view`):**  
   Extrae los datos de `request.POST` y delega la ejecución del trámite al Service Layer. No contiene SQL ni reglas de negocio.

5. **Service Layer / Trámite del negocio (`entregas/services.py` ➔ `registrar_pedido`):**  
   Ejecuta el trámite creando la instancia en la base de datos usando el ORM (`Pedido.objects.create(...)`). Asigna el estado inicial ("Registrado") y un ETA de mentira en este momento.

6. **Base de Datos / ORM en `entregas/models.py` ➔ `Pedido`:**  
   El ORM de Django mapea el objeto y ejecuta el `INSERT` en SQLite, retornando el objeto con su `id` que actua como su folio asignado automáticamente.

7. **Respuesta HTTP / Patrón PRG con `views.py`:**  
   La vista recibe el objeto `pedido` recién creado y responde con una redirección HTTP 302: `redirect('/pedidos/<id>/')`.

8. **Petición GET / Seguimiento (`seguimiento_view` ➔ `seguimiento.html`):**  
   El navegador sigue la redirección ejecutando un `GET /pedidos/<id>/`. La vista consulta `services.obtener_pedido(id)` y pasa el objeto a la _Template View_ `seguimiento.html`, la cual renderiza la pantalla sin ejecutar ningún `SELECT` o consulta a la base de datos.
