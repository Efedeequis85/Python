import conectar

def eliminar(entradas):

    id = entradas['idEntrada'].get()
    consulta = f"DELETE FROM usuarios WHERE id = {id}"
    
    api = conectar.conectar()
    cursor = api.cursor()
    cursor.execute('use salvadora')
    cursor.execute(consulta)
    api.commit()

    cursor.close()
    api.close()

    entradas['comentarioEntrada'].set(f"Registro [{id}] eliminado.")
