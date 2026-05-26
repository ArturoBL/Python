from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

# Carpeta de templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):

    elementos = [
        "Manzana",
        "Naranja",
        "Plátano",
        "Fresa"
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "titulo": "Lista de Frutas",
            "elementos": elementos
        }
    )