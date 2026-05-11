import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

'''
Este ejemplo muestra el funcionamiento del middleware aplicado a la detección de un archivo de
configuración que indicará si se tiene acceso al sistema o no. En caso de no existir el archivo
de configuración se podrá redirigir a un endpoint de setup.
'''

app = FastAPI()

ARCHIVO_CONTROL = "activo.txt"

# Agrupa aquí todas las rutas según el caso que las habilita
RUTAS_CON_ARCHIVO = {"/activo", "/usuarios", "/reportes"}
RUTAS_SIN_ARCHIVO = {"/inactivo", "/mantenimiento"}


class RedirigirSegunArchivoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        archivo_existe = os.path.exists(ARCHIVO_CONTROL)
        path = request.url.path

        # Desde "/" redirige al home correcto
        if path == "/":
            destino = "/activo" if archivo_existe else "/inactivo"
            return RedirectResponse(url=destino)

        # Bloquea rutas que requieren el archivo cuando este no existe
        if path in RUTAS_CON_ARCHIVO and not archivo_existe:
            return JSONResponse(
                status_code=403,
                content={"detalle": f"'{ARCHIVO_CONTROL}' no existe. Sistema en mantenimiento."},
            )

        # Bloquea rutas de mantenimiento cuando el archivo sí existe
        if path in RUTAS_SIN_ARCHIVO and archivo_existe:
            return JSONResponse(
                status_code=403,
                content={"detalle": f"'{ARCHIVO_CONTROL}' existe. Sistema en línea."},
            )

        return await call_next(request)


app.add_middleware(RedirigirSegunArchivoMiddleware)


# ── Endpoints normales ────────────────────────────────────────────────────────
@app.get("/activo")
async def endpoint_activo():
    return {"estado": "ACTIVO", "mensaje": "Sistema en línea."}

@app.get("/usuarios")
async def endpoint_usuarios():
    return {"estado": "ACTIVO", "usuarios": ["ana", "luis", "marta"]}

@app.get("/reportes")
async def endpoint_reportes():
    return {"estado": "ACTIVO", "reportes": ["reporte_01.pdf", "reporte_02.pdf"]}


# ── Endpoints de mantenimiento ────────────────────────────────────────────────
@app.get("/inactivo")
async def endpoint_inactivo():
    return {"estado": "INACTIVO", "mensaje": "Sistema en mantenimiento."}

@app.get("/mantenimiento")
async def endpoint_mantenimiento():
    return {"estado": "INACTIVO", "mensaje": "Vuelve pronto. Estamos trabajando en mejoras."}
