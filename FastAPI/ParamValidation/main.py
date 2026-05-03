from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator, model_validator
import re

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    edad: int
    email: str
    password: str

    # Validación personalizada de nombre
    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        return v

    # Validación personalizada de edad
    @field_validator("edad")
    @classmethod
    def edad_valida(cls, v):
        if v < 18:
            raise ValueError("Debes ser mayor de edad")
        if v > 120:
            raise ValueError("Edad no válida")
        return v

    # Validación personalizada de email (regex simple)
    @field_validator("email")
    @classmethod
    def email_valido(cls, v):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(pattern, v):
            raise ValueError("Email no válido")
        return v

    # Validación personalizada de password
    @field_validator("password")
    @classmethod
    def password_seguro(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Debe incluir una mayúscula")
        if not re.search(r"[0-9]", v):
            raise ValueError("Debe incluir un número")
        return v

    # Validación cruzada (entre campos)
    @model_validator(mode="after")
    def validar_coherencia(self):
        if self.nombre.lower() in self.password.lower():
            raise ValueError("La contraseña no debe contener el nombre")
        return self

@app.post("/registro")
def registrar_usuario(usuario: Usuario):
    return {
        "mensaje": "Usuario válido",
        "usuario": usuario
    }
