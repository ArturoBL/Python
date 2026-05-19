from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="Demo FastAPI con Archivos Estáticos")

# Montar el directorio 'static' para servir archivos estáticos
# Todos los archivos en /static estarán disponibles en la URL /static/...
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    """Ruta principal: devuelve el archivo HTML estático."""
    return FileResponse("static/index.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)