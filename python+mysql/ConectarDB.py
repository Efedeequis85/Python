import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="user",
        password="pass",
        database = "DB"
        )

    return conexion
