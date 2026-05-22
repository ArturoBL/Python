from sqlalchemy import select
from database import Session
from models.usuario import Usuario

session = Session()

stmt = (
    select(Usuario)
    .where(Usuario.id >3)
    .order_by(Usuario.nombre)
)

usuarios = session.execute(stmt).scalars().all()

for usuario in usuarios:
    print(usuario.id,usuario.nombre)

session.close()