from sqlalchemy import text
from database import Session

session = Session()

stmt = text("""
    SELECT id, nombre
    FROM usuarios
    WHERE id > 3
""")

resultados = session.execute(stmt)

for fila in resultados:
    print(fila.id, fila.nombre)    

session.close()    