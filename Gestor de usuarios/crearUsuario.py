import conectar

def crear(entradas):
    api = conectar.conectar()
    cursor = api.cursor()
    cursor.execute('use salvadora')

    datos = [entradas['idEntrada'], entradas['nombreEntrada'], entradas['apellidoEntrada'], entradas['passEntrada'], entradas['direccionEntrada']]
    consulta = f'INSERT INTO usuarios (id, nombre, apellido, contrasenia, direccion) VALUES ({datos[0].get()}, "{datos[1].get()}", "{datos[2].get()}", "{datos[3].get()}", "{datos[4].get()}")'
    
    cursor.execute(consulta)
    api.commit()

    cursor.close()
    api.close()

    entradas['comentarioEntrada'].set('Usuario creado.')
