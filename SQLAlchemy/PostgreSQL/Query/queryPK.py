from sqlalchemy import select,and_
from database import Session
from models.usuario import Usuario

session = Session()

usuario = session.get(Usuario, 3)

print(usuario.id,usuario.nombre)

session.close()