import mysql.connector

def crear():
    conexion = mysql.connector.connect(host="127.0.0.1", user="user", password="pass")

    cursor = conexion.cursor()
    cursor.execute("CREATE DATABASE salvadora")
    cursor.execute("use salvadora")

    consulta = '''CREATE TABLE usuarios(
        id INT NOT NULL,
        nombre VARCHAR(10) NOT NULL,
        apellido VARCHAR(10) NOT NULL,
        contrasenia VARCHAR(10) NOT NULL,
        direccion VARCHAR(10) NOT NULL
    )'''
    cursor.execute(consulta)

    return conexion
