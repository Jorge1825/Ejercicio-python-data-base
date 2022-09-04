import modelos.conection as conexion 


conec = conexion.conecction()
database = conec[0]
cursor = conec[1]



class Vehiculo:
    
    def __init__(self,marca = str("NULL"), modelo = str("NULL"), precio =float(0)) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    

    
    
    def guardar(self):
        sql = "insert into vehiculos () values (null,%s, %s, %s)"
        auto =(self.marca, self.modelo, self.precio)
        
        cursor.execute(sql,auto)
        database.commit()
        return [cursor.rowcount, self]
    
    
    def eliminar(self, codigo):
        
        eliminar = f"delete from vehiculos where id = {codigo}"

        cursor.execute(eliminar)
        database.commit()
        
        return [cursor.rowcount, self]
        
    
    def listar(self):
        listar = "select * from vehiculos"
        
        cursor.execute(listar)
        
        return cursor.fetchall()
    
    


auto1 = Vehiculo("Ferrari", "y46")

