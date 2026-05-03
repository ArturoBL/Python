from fastapi import FastAPI

'''
    Installation:
    pip install -r requirements.txt

    Run:
    b

    Test:
    http://127.0.0.1:8000       With default Port
    http://127.0.0.1:8000/docs  Swagger
    http://127.0.0.1:8000/redoc

'''

app = FastAPI()

# Endpoint básico
@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo desde FastAPI"}
