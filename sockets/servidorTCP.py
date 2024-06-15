# Los sockets se usan para enviar datos a traves de la red de un equipo a otro.
import socket

import socket

# AF_INET para indicar que sera un socket IPV4
# SOCK_STREAM para indicar que sera TCP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Interefaz y puerto donde recibira los datos
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Podemos indicarle el numero maximo de conexiones que queremos que reciba
server_socket.listen(1)

while True:
  # El metodo accept bloquea la ejecucion del programa hasta que se reciba una conexion. Devuelve el socket con el que interactuamos con el cliente y su respectiva direccion
  clienteSocket, clienteDir = server_socket.accept()

  try:
    while True:
    data = clienteSocket.recv(1024)

    # Que no se hallan recibido datos puede ser señal de que se cerro la conexion
      if not data:
        break
      print(f"Datos: {data.decode()}")

      # Send back a response
      client_socket.sendall(b"Datos recibidos: " + data)

  finally:
    # Para finalizar siempre sebemos cerrar el socker    
    clienteSocket.close()
