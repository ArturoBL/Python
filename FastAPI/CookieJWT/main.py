from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from fastapi import FastAPI, HTTPException, Request, Response, Cookie
from pydantic import BaseModel

# =========================================================
# CONFIGURACIÓN
# =========================================================

SECRET_KEY = "mi_clave_secreta_super_segura"
ALGORITHM = "HS256"
SESSION_MINUTES = 5

app = FastAPI()

# =========================================================
# BASE DE DATOS SIMULADA
# =========================================================

# Simula usuarios almacenados en BD
FAKE_USERS_DB = {
    "arturo": {
        "password": "123456",
        "nombre": "Arturo",
        "rol": "admin"
    },
    "juan": {
        "password": "abc123",
        "nombre": "Juan Pérez",
        "rol": "usuario"
    }
}

# Simula sesiones almacenadas en memoria
# En producción esto normalmente estaría en Redis o BD
SESSIONS = {}

# =========================================================
# MODELOS
# =========================================================

class LoginRequest(BaseModel):
    usuario: str
    password: str


# =========================================================
# FUNCIONES JWT
# =========================================================

def crear_token(usuario: str):
    expiracion = datetime.now(timezone.utc) + timedelta(minutes=SESSION_MINUTES)

    payload = {
        "sub": usuario,
        "exp": expiracion
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token, expiracion


def validar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="La sesión ha caducado"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )


# =========================================================
# ENDPOINT LOGIN
# =========================================================

@app.post("/login")
def login(data: LoginRequest, response: Response):

    usuario_db = FAKE_USERS_DB.get(data.usuario)

    # Validar usuario y password
    if not usuario_db or usuario_db["password"] != data.password:
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )

    # Crear JWT
    token, expiracion = crear_token(data.usuario)

    # Guardar sesión simulada
    SESSIONS[token] = {
        "usuario": data.usuario,
        "password": data.password,
        "expira": expiracion
    }

    # Crear cookie de sesión
    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        max_age=SESSION_MINUTES * 60,
        expires=SESSION_MINUTES * 60,
        samesite="lax"
    )

    return {
        "mensaje": "Login correcto",
        "token": token,
        "expira": expiracion.isoformat()
    }


# =========================================================
# ENDPOINT PROTEGIDO
# =========================================================

@app.get("/datos")
def obtener_datos(session_token: Optional[str] = Cookie(default=None)):

    # Verificar cookie
    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="No existe sesión activa"
        )

    # Validar JWT
    payload = validar_token(session_token)

    # Verificar sesión almacenada
    sesion = SESSIONS.get(session_token)

    if not sesion:
        raise HTTPException(
            status_code=401,
            detail="Sesión no encontrada"
        )

    # Obtener usuario y password simulando acceso a BD
    usuario = sesion["usuario"]
    password = sesion["password"]

    # Simulación de consulta a BD usando credenciales
    usuario_db = FAKE_USERS_DB.get(usuario)

    if not usuario_db or usuario_db["password"] != password:
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    return {
        "mensaje": "Sesión válida",
        "usuario": usuario,
        "nombre": usuario_db["nombre"],
        "rol": usuario_db["rol"]
    }


# =========================================================
# LOGOUT
# =========================================================

@app.post("/logout")
def logout(response: Response,
           session_token: Optional[str] = Cookie(default=None)):

    if session_token in SESSIONS:
        del SESSIONS[session_token]

    response.delete_cookie("session_token")

    return {
        "mensaje": "Sesión cerrada"
    }