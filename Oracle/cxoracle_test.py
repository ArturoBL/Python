import cx_Oracle

'''
1. Instalar oracle instant client de acuerdo a plataforma (32 o 64 bits) 
    o en su defecto copiar dlls del instant client en la carpeta de python (ver imagen "Copiar dlls.png") o
    en la carpeta correspondiente al entorno virtual (\venv\Scripts)
2. Activar el entorno virtual (si aplica).
3. Importar librería cx_Oracle
'''
try:
    DBUser = "your user"
    DBPassword = "your password"
    DBHost = "your host"
    DBPort = 1521   #default port
    OracleServiceName = "your service"
    dsnString = f"{DBHost}:{DBPort}/{OracleServiceName}"
    connection = cx_Oracle.connect(user=DBUser, password=DBPassword,dsn=dsnString)

    row1 = [2, "Second"]
    cursor = connection.cursor()
    cursor.execute("insert into tmp_pruebainsert (id, data) values (:1, :2)", row1)
    rowid1 = cursor.lastrowid
    connection.commit()

    print("Row 1:", row1)
    print("Rowid 1:", rowid1)
finally:    
    cursor.close()
    connection.close()
