from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

'''
Para activar el cliente en VSCODE:

1. Ctrl + Shift + P
2. Buscar y seleccionar: MCP: Add Server...
3. Seleccionar: HTTP (HTTP or Server sent events)
4. Escribir la URL con la ruta http://ip:puerto/mcp
5. Escribir el nombre de identificación del servicio MCP.
6. Seleccionar el target (Global o workspace, si se elije workspace se crea el archivo mcp.json en la carpeta del proyecto).
7. Si se configura como workspace se generará el archivo mcp.json con la configuración del servicio MCP en la carpeta del proyecto, si se configura como global se guardará la configuración en el almacenamiento global de VSCODE.
7. En la barra de chat de agente verificar que está activado y se encontraron las tools expuestas mediante el icono de herramientas.
8. En caso de cambios se puede reiniciar dando click al botón de herramientas y en la lista de herramientas en el icono de engrane
, se abre el json con la configuración del MCP, debajo de "servers" aparecen opciones para detener, iniciar, reiniciar servicio, se puede reiniciar para actualizar lista de herramientas.
'''


app = FastAPI(
    title="Servidor MCP de Ejemplo",
    version="1.0.0"
)

@app.get("/resource/mainschema", operation_id="get_main_schema")
async def mainschema():
    return {"mainschema": "greenbox"}

@app.get("/resource/schemas", operation_id="get_schemas")
async def schemas():
    return {"schemas": ["greenbox", "postgres", "public"]}

@app.get("/resource/tables", operation_id="get_tables")
def tables():
    return {"tables": ["empleados","departamentos","ordenes_compra"]}




# Crear servidor MCP a partir de la aplicación FastAPI
mcp = FastApiMCP(
    app,
    name="Servidor MCP de Ejemplo"
)

# Agregar rutas MCP
mcp.mount()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
    