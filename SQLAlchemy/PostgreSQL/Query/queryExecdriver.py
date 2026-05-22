from sqlalchemy import create_engine
from database import engine


with engine.connect() as conn:

    result = conn.exec_driver_sql(
        "SELECT id, nombre FROM usuarios"
    )

    for row in result:
        print(row.id, row.nombre)
    
    conn.close()
