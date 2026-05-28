from fastapi import FastAPI, Response, Cookie
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root(response: Response):
    response = JSONResponse(content={"msg":"Sesión iniciada"})
    response.set_cookie(key="username",value="adminuser")
    return response

@app.get("/data")
def data(username: str =Cookie()):
    return username

@app.get("/logout")
def data(response: Response,username: str =Cookie()):
    response.delete_cookie("username")
    return {
        "msg": "Sesión cerrada"
    }