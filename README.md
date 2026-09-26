# Plataforma Empresa de Entregas (Aplicación Web Django)

Proyecto de arquitectura web desarrollado para la materia de Tópicos de Selección en Tecnologías Web y Móviles.

## Integrantes del Equipo

## Ejecutar el proyecto en local

### 1. Instalar dependencias de Python (Django)

```bash
pip install django
```

### 2. Aplicar las migraciones a la base de datos local

```bash
python manage.py migrate
```

### 3. (Opcional) Compilar estilos de Tailwind CSS con Node.js

```bash
npm install
npm run build:css
```

### 4. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Accede en tu navegador a: **`http://127.0.0.1:8000/pedidos/`**

---

## Avance de Notas

- **[Notas del Día 1](notas/dia1.md):** Tabla de análisis de los 7 inconvenientes del caso atados a las capacidades nativas de Django y patrones no reinventados.
- **[Notas del Día 2](notas/dia2.md):** Diagrama y flujo del camino de la petición `POST /pedidos` atraviesando Middlewares, Front Controller (`urls.py`), Page Controller (`views.py`), Service Layer (`services.py`), ORM (`models.py`) y la redirección con el patrón _PRG (Post-Redirect-Get)_.
