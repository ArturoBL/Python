from database import engine, Session, Base
from models.Obras import Obra
from models.Presupuestos import Presupuesto

session = Session()
obra = session.get(Obra, 1)
print("Obra:",obra.nombre)

for p in obra.presupuestos:
    print("Presupuesto:",p.descripcion)

session.close()