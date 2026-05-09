import oracledb

# Instant client location
ld = "C:\\Instantclient_11_2"
DBUser = "your user"
DBPass = "your password"
DBPort = 1521
DBHost = "your host"
DBService = 'service name'
try:
    oracledb.init_oracle_client(lib_dir=ld)
    params = oracledb.ConnectParams(host=DBHost, port=DBPort, service_name=DBService)
    connection = oracledb.connect(user=DBUser, password=DBPass, params=params)
    cursor = connection.cursor()

    row = self.QueryRow(cursor,f"""Select no_empleado, status
                                                from empleados
                                                where lower(e_mail) = lower('myemail@email.com')
                                                        """)
    if row:
        noempsol = row[0]
        print("Empleado:",noempsol)
finally:            
    cursor.close()
    connection.close

