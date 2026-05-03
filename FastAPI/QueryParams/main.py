from fastapi import FastAPI

app = FastAPI()

# Endpoint básico
@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo desde FastAPI"}

# Endpoint con parámetro en la URL
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola, {nombre}"}

# Endpoint con parámetros query
@app.get("/suma")
def sumar(a: int, b: int):
    return {"resultado": a + b}
