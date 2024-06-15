import mysql.connector

def crear():
    crearBase = "CREATE DATABASE DB"
    crearTabla = '''CREATE TABLE usuarios(TABLA)'''

    conexion = mysql.connector.connect(host="DireccionBaseDeDatos", user="user", password="pass")
    cursor = conexion.cursor()

    cursor.execute(crearBase)
    cursor.execute("use DB")
    cursor.execute(crearTabla)

    return conexion
