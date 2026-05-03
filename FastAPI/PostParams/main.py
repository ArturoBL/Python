from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos el modelo de datos que recibirá el POST
class Datos(BaseModel):
    nombre: str
    edad: int

# Endpoint POST
@app.post("/usuario")
def crear_usuario(datos: Datos):
    return {
        "mensaje": f"Usuario {datos.nombre} creado",
        "edad_en_5_anios": datos.edad + 5
    }
