from database import SessionLocal
from models.usuario import Usuario

session = SessionLocal()

usuarios = [
    Usuario(nombre="Juan", correo="juan@email.com"),
    Usuario(nombre="María", correo="maria@email.com"),
    Usuario(nombre="Pedro", correo="pedro@email.com")
]

session.bulk_save_objects(usuarios)
session.commit()