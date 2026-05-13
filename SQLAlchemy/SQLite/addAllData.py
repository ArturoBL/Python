from database import SessionLocal
from models.usuario import Usuario

session = SessionLocal()

# Lista de registros
usuarios = [
    Usuario(id = 2, nombre="Arturo", correo="arturo@email.com"),
    Usuario(id = 3, nombre="Ana", correo="ana@email.com"),
    Usuario(id = 4, nombre="Luis", correo="luis@email.com")
]

# Insertar todos
session.add_all(usuarios)

# Confirmar cambios
session.commit()

print("Registros insertados")