import conectar

def buscar(entradas):
    api = conectar.conectar()
    cursor = api.cursor()
    cursor.execute('use salvadora')

    consulta = f"SELECT * FROM usuarios WHERE id = {entradas['idEntrada'].get()}"
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    if(resultado == []):
        entradas['comentarioEntrada'].set('Usuario no encontrado.')
    else:
        entradas['comentarioEntrada'].set('Usuario encontrado.')
        for elemento in resultado:
            entradas['nombreEntrada'].set(elemento[1])
            entradas['apellidoEntrada'].set(elemento[2])
            entradas['passEntrada'].set(elemento[3])
            entradas['direccionEntrada'].set(elemento[4])
        
    cursor.close()
    api.close()
