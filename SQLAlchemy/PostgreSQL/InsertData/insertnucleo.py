from database import engine, Session, Base
from models.usuario import Usuario
from sqlalchemy import insert

session = Session()

stmt = insert(Usuario).values(nombre="Pedro", correo="pedro@ejemplo.com")
session.execute(stmt)
session.commit()
session.close()