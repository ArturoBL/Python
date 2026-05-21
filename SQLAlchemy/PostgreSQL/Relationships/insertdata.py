from database import engine, Session, Base
from models.Obras import Obra
from models.Presupuestos import Presupuesto

session = Session()

obra = Obra(nombre="Edificio Central")
p1 = Presupuesto(descripcion="Cancelería fachada")
p2 = Presupuesto(descripcion="Ventanas aluminio")

# Relacionar objetos
obra.presupuestos.append(p1)
obra.presupuestos.append(p2)

session.add(obra)

session.commit()
session.close()
