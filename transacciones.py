import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port ='5432',
                 database='test_db')
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Maria', 'Esparza', 'Mezpar@gmail.com')
    cursor.execute(sentencia,valores)
    conexion.commit()
    print('Termina transaccion')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo roolback: {e}')
finally:
    conexion.close()