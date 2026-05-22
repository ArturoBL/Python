from sqlalchemy import select,and_
from database import Session
from models.usuario import Usuario

session = Session()

stmt = select(Usuario).where(
    and_(
        Usuario.nombre == 'Pedro',
        Usuario.id > 3
    )
)

usuarios = session.execute(stmt).scalars().all()
for usuario in usuarios:
    print(usuario.id,usuario.nombre)

session.close()