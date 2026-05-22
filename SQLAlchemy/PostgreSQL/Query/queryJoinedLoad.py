from database import Session
from models.Obras import Obra
from models.Presupuestos import Presupuesto
from sqlalchemy import select
from sqlalchemy.orm import joinedload

session = Session()

stmt = (
    select(Presupuesto)
    .options(joinedload(Presupuesto.obra))
)

Presupuestos = session.scalars(stmt).all()

for p in Presupuestos:
    print(
            p.descripcion,
            p.obra.nombre
        )

session.close()    