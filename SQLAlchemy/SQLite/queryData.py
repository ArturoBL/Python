from database import SessionLocal
from models.usuario import Usuario

# Crear sesión
session = SessionLocal()

usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario.id, usuario.nombre, usuario.correo)
