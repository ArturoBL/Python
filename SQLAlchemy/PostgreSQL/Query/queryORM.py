from database import Session
from models.usuario import Usuario

session = Session()

usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario.nombre)

session.close()    