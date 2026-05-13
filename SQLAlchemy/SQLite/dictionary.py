from sqlalchemy import insert
from database import SessionLocal
from models.usuario import Usuario

session = SessionLocal()


datos = [
    {"nombre": "Carlos", "correo": "carlos@email.com"},
    {"nombre": "Laura", "correo": "laura@email.com"},
    {"nombre": "Elena", "correo": "elena@email.com"},
]

session.execute(insert(Usuario), datos)
session.commit()