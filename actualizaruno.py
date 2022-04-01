import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port ='5432',
                 database='test_db')
try:
    
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET  nombre = %s, email = %s WHERE id_persona = %s'
            valores = ('Juanastro', 'Juanastroo@mai.com', 1)
            cursor.execute(sentencia, valores)
            #Guardamos la info en la base de datos, ya no es necesario con el with
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio un error: {e}')
conexion.close()