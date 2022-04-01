import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port ='5432',
                 database='test_db')
try:
    
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona where id_persona IN %s'
            #Se usa la coma para indicar que es una tupla, en este caso es una tupla de tuplas
            llaves_primarias = ((1,2,3),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')
conexion.close()