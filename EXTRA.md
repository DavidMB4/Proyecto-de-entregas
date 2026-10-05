# Actividad para puntos extra — Retos sobre la ruta de Django

## Reto 1 — La ruta en todas las computadoras (1 punto)

### Evidencia de `sys.prefix` entorno de Python activo

#### Windows:

```text
C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.12_3.12.2800.0_x64__qbz5n2kfra8p0
```

### Evidencia de "/entregas/estado/" en el navegador JSON

Respuesta obtenida en la URL `http://127.0.0.1:8000/entregas/estado/`:

```json
{
  "servicio": "entregas",
  "version": 1,
  "medios_disponibles": ["camioneta", "moto", "bicicleta", "dron"]
}
```

### 3. Diferencia de comandos entre Windows y Linux/macOS (Respuesta escrita)

En **Windows (PowerShell)**, el entorno virtual se activa mediante el script `.venv\Scripts\Activate.ps1` o usando el lanzador `py` en lugar de `python3`.

En **Linux y macOS**, la activación se realiza mediante el comando `source .venv/bin/activate` utilizando la ruta ejecutable en `/bin/` de Unix. Además, el guardado de dependencias en Windows PowerShell requiere especificar el formato UTF-8 (`pip freeze | Out-File -Encoding utf8 requirements.txt`) para evitar problemas de codificación de caracteres.
