import mysql.connector
from tkinter import *

class Api:
    def __init__(self, host, db, tabla, user, passwd):
        self.host = host
        self.db = db
        self.tabla = tabla
        self.user = user
        self.passwd = passwd

    def _crearDB(self):
        conexion = mysql.connector.connect(host=self.host, user=self.user, password=self.passwd)
        cursor = conexion.cursor()

        tabla = f'''CREATE TABLE {self.tabla}(
            id INT NOT NULL,
            nombre VARCHAR(10) NOT NULL,
            apellido VARCHAR(10) NOT NULL,
            contrasenia VARCHAR(10) NOT NULL
        )'''

        cursor.execute(f"CREATE DATABASE {self.db}")
        cursor.execute(f"USE {self.db}")
        cursor.execute(tabla)

        cursor.close()
        conexion.close()

        return 0

    def conectar(self):
        conexion = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.passwd,
        database = self.db
        )
        return conexion

class Crud:
    def __init__(self, api):
        self.api = api
    
    def _crear(self, datos):
        api = self.api.conectar()
        cursor = api.cursor()
        cursor.execute(f'USE {self.api.db}')

        consulta = f'INSERT INTO {self.api.tabla} (id, nombre, apellido, contrasena) VALUES ({datos["idEntrada"].get()}, "{datos["nombreEntrada"].get()}", "{datos["apellidoEntrada"].get()}", "{datos["passEntrada"].get()}")'
    
        cursor.execute(consulta)
        api.commit()

        cursor.close()
        api.close()

        datos['comentarioEntrada'].set('Usuario creado.')

    def _buscar(self, datos):
        api = self.api.conectar()
        cursor = api.cursor()
        cursor.execute(f'USE {self.api.db}')

        consulta = f"SELECT * FROM {self.api.tabla} WHERE id = {datos['idEntrada'].get()}"
        cursor.execute(consulta)
        resultado = cursor.fetchall()

        if(resultado == []):
            datos['comentarioEntrada'].set('Usuario no encontrado.')
        else:
            datos['comentarioEntrada'].set('Usuario encontrado.')
            for elemento in resultado:
                datos['nombreEntrada'].set(elemento[1])
                datos['apellidoEntrada'].set(elemento[2])
                datos['passEntrada'].set(elemento[3])
            
        cursor.close()
        api.close()

    def _actualizar(self, datos):
        api = self.api.conectar()
        cursor = api.cursor()
        

        consulta = f'UPDATE {self.api.tabla} SET id = {datos["idEntrada"].get()},nombre = "{datos["nombreEntrada"].get()}", apellido = "{datos["apellidoEntrada"].get()}", contrasena = "{datos["passEntrada"].get()}" WHERE id = "{datos["idEntrada"].get()}"'

        cursor.execute(f'USE {self.api.db}')
        cursor.execute(consulta)
        api.commit()

        cursor.close()
        api.close()

        datos['comentarioEntrada'].set("Usuario Actualizado.")

    def _eliminar(self, datos):
        api = self.api.conectar()
        cursor = api.cursor()

        id = datos['idEntrada'].get()
        consulta = f"DELETE FROM usuarios WHERE id = {id}"
        
        cursor.execute(f'USE {self.api.db}')
        cursor.execute(consulta)
        api.commit()

        cursor.close()
        api.close()

        datos['comentarioEntrada'].set(f"Registro [{id}] eliminado.")

    def _limpiar(self, datos):
        datos["idEntrada"].set("")
        datos["nombreEntrada"].set("")
        datos["passEntrada"].set("")
        datos["apellidoEntrada"].set("")
        datos["comentarioEntrada"].set("")

    def iniciarInterfaz(self):        
        raiz = Tk()
        raiz.title("USUARIOS")
        raiz.geometry("430x330")

        miFrame = Frame()
        miFrame.pack()

        datos = {
            'idEntrada' : StringVar(),
            'nombreEntrada' : StringVar(),
            'passEntrada' : StringVar(),
            'apellidoEntrada' : StringVar(),
            'comentarioEntrada' : StringVar()
        }

        ######################################## ENTRADAS ########################################
        idLabel = Label(miFrame, text="id")
        idLabel.grid(row=1, column=0)
        idEntry = Entry(miFrame, textvariable=datos['idEntrada'])
        idEntry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        nombreLabel = Label(miFrame, text="Nombre")
        nombreLabel.grid(row=2, column=0)
        nombreEntry = Entry(miFrame, textvariable=datos['nombreEntrada'])
        nombreEntry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        passLabel = Label(miFrame, text="Contraseña")
        passLabel.grid(row=3, column=0)
        passEntry = Entry(miFrame, textvariable=datos['passEntrada'])
        passEntry.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        apellidoLabel = Label(miFrame, text="Apellido")
        apellidoLabel.grid(row=4, column=0)
        apellidoEntry = Entry(miFrame, textvariable=datos['apellidoEntrada'])
        apellidoEntry.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        comentariosLabel = Label(miFrame, text="Comentario")
        comentariosLabel.grid(row=5, column=0)
        comentariosEntry = Entry(miFrame, textvariable=datos['comentarioEntrada'])
        comentariosEntry.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        botonLimpiar = Button(miFrame, text="LIMPIAR", command=lambda:self._limpiar(datos))
        botonLimpiar.grid(row=6, column=0, padx=10, pady=10)

        ######################################### BOTONES ######################################### 
        botonActualizar = Button(miFrame, text="CREAR", command=lambda:self._crear(datos))
        botonActualizar.grid(row=7, column=0, padx=10, pady=10)

        botonActualizar = Button(miFrame, text="BUSCAR", command=lambda:self._buscar(datos))
        botonActualizar.grid(row=7, column=1, padx=10, pady=10)

        botonActualizar = Button(miFrame, text="ACTUALIZAR", command=lambda:self._actualizar(datos))
        botonActualizar.grid(row=7, column=2, padx=10, pady=10)

        botonActualizar = Button(miFrame, text="ELIMINAR", command=lambda:self._eliminar(datos))
        botonActualizar.grid(row=7, column=3, padx=10, pady=10)

        raiz.mainloop()
