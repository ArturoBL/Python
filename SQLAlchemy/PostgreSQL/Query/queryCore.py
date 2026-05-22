from sqlalchemy import Table, MetaData, select
from database import engine

metadata = MetaData()

usuarios = Table(
    "usuarios",
    metadata,
    autoload_with=engine
)

stmt = select(usuarios)

with engine.connect() as conn:
    resultados = conn.execute(stmt)

    for fila in resultados:
        print(fila.nombre)