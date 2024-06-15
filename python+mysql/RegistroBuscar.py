import conectar

def buscar(datos):
    consulta = f"SELECT * FROM usuarios WHERE id = {datos['identificador']}"
    
    conn = conectar.conectar()
    cursor = conn.cursor()

    cursor.execute('use base-de-datos')
    cursor.execute(consulta)
    resultado = cursor.fetchall()

    if(resultado == []):
        datos['comentario'].set('Usuario no encontrado.')
    else:
        datos['comentario'].set('Usuario encontrado.')
        for elemento in resultado:
            datos['dato'].set(elemento[1])
            datos['dato'].set(elemento[2])
            datos['dato'].set(elemento[3])
            datos['dato'].set(elemento[4])
        
    cursor.close()
    conn.close()
