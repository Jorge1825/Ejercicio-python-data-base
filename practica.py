
import mysql.connector

# ------------------BASE DE DATOS CON PYTHON    


database = mysql.connector.connect(host="localhost", user="root", passwd="", db="Vehiculos")

micursor = database.cursor(buffered=True)

micursor.execute("""
                 CREATE TABLE IF NOT EXISTS vehiculos( 
                 id int AUTO_INCREMENT not null,
                 Marca VARCHAR(50) not null,
                 Modelo VARCHAR(50) NOT NULL,
                 Precio float(10,2) NOT NULL,
                 constraint pk_Vehiculos primary key(id)
                )
                 
                 """)


""" 
micursor.execute('''
                 insert into vehiculos (Marca, Modelo, Precio) values ('Toyota', 'Corolla', '45000')
                 ''')

 """
 
 
"""  
vehiculos = [("Ferrari", "y46", "100000"),
             ("Mercedes", "fr4", "356400"),
             ("Audi", "a4", "250000")
             ]
     

micursor.executemany("insert into vehiculos () values (null,%s, %s, %s)", vehiculos)
 """

#Mostrar datos
micursor.execute("select * from vehiculos where marca = 'Ferrari'")
resultado = micursor.fetchall()


for i in resultado:
    print(i)

#Para un dato especifico
micursor.execute("select * from vehiculos where marca = 'Ferrari'")
unregistro = micursor.fetchone()
print(unregistro)



#borrar datos

micursor.execute("delete from vehiculos where marca = 'Audi'")


#Ver los datos afectados despues de la operacion
print(micursor.rowcount, " registros afectados")


#Actualizar datos
micursor.execute("update vehiculos set modelo = 'gfdg554' where marca = 'Ferrari'")
print(micursor.rowcount, " registros actualizados")






database.commit()
database.close()

