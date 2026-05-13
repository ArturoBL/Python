from database import SessionLocal
from models.usuario import Usuario
import pandas as pd
from sqlalchemy import insert


session = SessionLocal()

df = pd.DataFrame([
    {"nombre": "A", "correo": "a@email.com"},
    {"nombre": "B", "correo": "b@email.com"},
])

session.execute(insert(Usuario), df.to_dict(orient="records"))
session.commit()