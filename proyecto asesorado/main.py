
import modelos.Vehiculo as model


auto = model.Vehiculo("Ferrari", "y46", 100000)

"""
guardar = auto.guardar()
print("Se guardo: ", guardar) """


#Eliminar un registro


result=auto.eliminar(5)
print(result)

lista=auto.listar()
for i in lista:
    print(i)





