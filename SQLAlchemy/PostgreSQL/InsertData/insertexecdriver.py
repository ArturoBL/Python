from database import engine,  Base

conn = engine.connect()

conn.exec_driver_sql(
        """
        INSERT INTO usuarios (nombre, correo)
        VALUES (%s, %s)
        """,
        ("Vanessa", "vanessa@ejemplo.com")
    )

conn.commit()
conn.close()

'''
Aquí los placeholders dependen del driver:

? → SQLite
%s → psycopg2/MySQL
:1 → Oracle
'''