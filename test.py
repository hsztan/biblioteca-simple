from psycopg2 import connect


connection = connect(user='postgres', password='mysql', 
                    database='semana_6', 
                    host='localhost', port=5432)

cursor = connection.cursor()
cursor.execute('SELECT * FROM mobile') # Ejecuta

#################################################

# readline (fetchone) - readlines (fetchall)
record = cursor.fetchall() # Muestra lo retornado
print(record)
