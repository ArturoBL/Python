from database import engine, Session, Base
from models.usuario import Usuario

session = Session()

usuarios = [
    Usuario(nombre="Luis", correo="luis@ejemplo.com"),
    Usuario(nombre="Maria", correo="maria@ejemplo.com")
]

session.add_all(usuarios)
session.commit()

# Cerrar sesión
session.close()