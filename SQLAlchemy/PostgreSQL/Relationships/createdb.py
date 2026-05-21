from database import engine, Base
from models.Obras import Obra
from models.Presupuestos import Presupuesto

# -----------------------------------------
# Crear base de datos
# -----------------------------------------
Base.metadata.create_all(bind=engine)