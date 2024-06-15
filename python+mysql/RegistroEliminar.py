import conectar

def eliminar(datos):
    id = datos['id']
    consulta = f"DELETE FROM usuarios WHERE id = {id}"
    
    conn = conectar.conectar()
    cursor = conn.cursor()

    cursor.execute('use DB')
    cursor.execute(consulta)
    conn.commit()

    cursor.close()
    conn.close()

    datos['comentarioEntrada'].set(f"[{id}] eliminado.")
