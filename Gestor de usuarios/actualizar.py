import conectar

def actualizar(entradas):
    api = conectar.conectar()
    cursor = api.cursor()
    cursor.execute('use salvadora')
    
    datos = [entradas['idEntrada'], entradas['nombreEntrada'], entradas['apellidoEntrada'], entradas['passEntrada'], entradas['direccionEntrada']]
    consulta = f'UPDATE usuarios SET id = {datos[0].get()},nombre = "{datos[1].get()}", apellido = "{datos[2].get()}", contrasenia = "{datos[3].get()}", direccion = "{datos[4].get()}" WHERE id = "{datos[0].get()}"'

    cursor.execute(consulta)
    api.commit()

    cursor.close()
    api.close()

    entradas['comentarioEntrada'].set("Usuario Actualizado")
