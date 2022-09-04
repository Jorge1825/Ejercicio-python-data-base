import mysql.connector



def conecction():
    database = mysql.connector.connect(host="localhost", user="root", passwd="", db="Vehiculos")
    micursor = database.cursor(buffered=True)
    
    return [database, micursor]


