from database import engine, Session, Base
from models.usuario import Usuario

session = Session()

# Crear registro, el id se autocalcula
nuevo_usuario = Usuario(    
    nombre="juan",
    correo="juan@gmail.com"
)

# Insertar
session.add(nuevo_usuario)

# Guardar cambios
session.commit()

# Mostrar ID generado
print(f"ID generado: {nuevo_usuario.id}")

# Cerrar sesión
session.close()