import buscar
import actualizar
import crearUsuario
import eliminarUsuario

from tkinter import *

def iniciar():

    raiz = Tk()
    raiz.title("USUARIOS")
    raiz.geometry("430x330")

    miFrame = Frame()
    miFrame.pack()

    entradas = {
        'idEntrada' : StringVar(),
        'nombreEntrada' : StringVar(),
        'passEntrada' : StringVar(),
        'apellidoEntrada' : StringVar(),
        'direccionEntrada' : StringVar(),
        'comentarioEntrada' : StringVar()
    }

    ######################################## ENTRADAS ########################################

    idLabel = Label(miFrame, text="id")
    idLabel.grid(row=1, column=0)
    idEntry = Entry(miFrame, textvariable=entradas['idEntrada'])
    idEntry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    nombreLabel = Label(miFrame, text="Nombre")
    nombreLabel.grid(row=2, column=0)
    nombreEntry = Entry(miFrame, textvariable=entradas['nombreEntrada'])
    nombreEntry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    passLabel = Label(miFrame, text="Contraseña")
    passLabel.grid(row=3, column=0)
    passEntry = Entry(miFrame, textvariable=entradas['passEntrada'])
    passEntry.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

    apellidoLabel = Label(miFrame, text="Apellido")
    apellidoLabel.grid(row=4, column=0)
    apellidoEntry = Entry(miFrame, textvariable=entradas['apellidoEntrada'])
    apellidoEntry.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

    direccionLabel = Label(miFrame, text="Direccion")
    direccionLabel.grid(row=5, column=0)
    direccionEntry = Entry(miFrame, textvariable=entradas['direccionEntrada'])
    direccionEntry.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

    comentariosLabel = Label(miFrame, text="Comentario")
    comentariosLabel.grid(row=6, column=0)
    comentariosEntry = Entry(miFrame, textvariable=entradas['comentarioEntrada'])
    comentariosEntry.grid(row=6, column=1, padx=10, pady=10, columnspan=2)

    ######################################### BOTONES ######################################### 
    botonActualizar = Button(miFrame, text="CREAR", command=lambda:crearUsuario.crear(entradas))
    botonActualizar.grid(row=7, column=0, padx=10, pady=10)

    botonActualizar = Button(miFrame, text="BUSCAR", command=lambda:buscar.buscar(entradas))
    botonActualizar.grid(row=7, column=1, padx=10, pady=10)

    botonActualizar = Button(miFrame, text="ACTUALIZAR", command=lambda:actualizar.actualizar(entradas))
    botonActualizar.grid(row=7, column=2, padx=10, pady=10)

    botonActualizar = Button(miFrame, text="ELIMINAR", command=lambda:eliminarUsuario.eliminar(entradas))
    botonActualizar.grid(row=7, column=3, padx=10, pady=10)

    raiz.mainloop()
