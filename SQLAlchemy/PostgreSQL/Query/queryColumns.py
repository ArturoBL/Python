from sqlalchemy import select
from database import Session
from models.usuario import Usuario

session = Session()

stmt = select(Usuario.id, Usuario.nombre)

resultados = session.execute(stmt).all()

for fila in resultados:
    print(fila.id, fila.nombre)

session.close()