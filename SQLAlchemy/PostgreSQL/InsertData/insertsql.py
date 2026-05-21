from database import engine, Session, Base
from sqlalchemy import text

session = Session()
sql = text("""
        INSERT INTO usuarios (nombre, correo)
        VALUES (:nombre, :correo)
    """)

'''
Aquí los placeholders dependen del driver:

? → SQLite
%s → psycopg2/MySQL
:1 → Oracle
'''

session.execute(
        sql,
        {
            "nombre": "Pao",
            "correo": "Pao@hotmail.com"
        }
    )

session.commit()
session.close()