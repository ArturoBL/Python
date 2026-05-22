from sqlalchemy import select
from database import Session
from models.usuario import Usuario

session = Session()

stmt = select(Usuario)

usuarios = session.execute(stmt).scalars().all()

for usuario in usuarios:
    print(usuario.nombre)

session.close()