from database import engine,  Base

datos = [
    ("Laura", "lau@correo.com"),
    ("Ana", "micorreo@correoprueba.com"),
    ("Luis", "ok@correook.com"),
]

with engine.begin() as conn:

    conn.exec_driver_sql(
        "INSERT INTO usuarios(nombre, correo) VALUES (%s, %s)",
        datos
    )
    conn.commit()
    conn.close()