from sqlalchemy import select,and_
from models.Obras import Obra
from models.Presupuestos import Presupuesto
from database import Session

session = Session()

stmt = (
    select(Obra, Presupuesto)
    .join(Presupuesto, Obra.id == Presupuesto.obra_id)
)

resultados = session.execute(stmt).all()

for Obra, Presupuesto in resultados:
    print(Obra.nombre, Presupuesto.descripcion)

session.close()