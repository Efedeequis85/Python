import conectar

def actualizar(datos):
    datos = [datos['nombre'], datos['user']]
    consulta = f'UPDATE usuarios SET dato = {datos[0]}, dato = "{datos[1]}"'

    conn = conectar.conectar()
    cursor = conn.cursor()

    cursor.execute('USE DB')
    cursor.execute(consulta)
    conn.commit()

    cursor.close()
    conn.close()

    datos['comentario'].set("Registro Actualizado")
