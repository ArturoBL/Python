from database import SessionLocal
from models.usuario import Usuario

session = SessionLocal()

# Crear registro
nuevo_usuario = Usuario(
    id = 1,
    nombre="Arturo",
    correo="arturo@email.com"
)

# Guardar
session.add(nuevo_usuario)
session.commit()

print("Usuario insertado")