from database import engine, Session, Base
from models.Obras import Obra
from models.Presupuestos import Presupuesto

session = Session()

presupuesto = session.get(Presupuesto, 1)
print("Presupuesto:",presupuesto.descripcion)
print("Obra:",presupuesto.obra.nombre)

session.close()