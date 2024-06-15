import conectar

def crear(entradas):
    datos = [entradas['nombre'], entradas['user']]
    consulta = f'INSERT INTO TABLA (espacio, espacio) VALUES ({datos[0]}, "{datos[1]}")'

    conn = conectar.conectar()
    cursor = conn.cursor()

    cursor.execute('USE DB')
    cursor.execute(consulta)
    conn.commit()

    cursor.close()
    conn.close()

    entradas['comentario'].set('Registro creado.')
