import sqlite3

#conecto con base de datos
conn = sqlite3.connect(":memory:")

#creo cursor
cursor = conn.cursor()

#creo tabla
cursor.execute("""CREATE TABLE currency
               (ID integer prumary key, name text, symbol text)""")

#inserto datros
cursor.execute("INSERT INTO currency VALUES (1, 'bla bla', '$')")

#guardo cambios 
conn.commit()

#consulto monedas en este caso
query = "SELECT * FROM currency"

#Busco el resultado
currencies = cursor.execute(query).fetchall()

print (currencies)

#Cierro conexion
conn.close()