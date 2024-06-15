# Con el cliente podemos conectarnos a un servidor TCP que este a al escucha

import socket

# AF_INET para indicar que sera un socket IPV4
# SOCK_STREAM para indicar que sera TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# El metodo conect recibe una tupla donde deben estar los datos del servidor
server_address = ('localhost', 12345)
sock.connect(server_address)

try:
  # Enviar datos al servidor
  message = "Hola servidor!"
  client_socket.sendall(message.encode())

  # El metodo recv bloquea la ejecucion del programa hasta que se reciban datos del servidor
  data = client_socket.recv(1024)
  print(f"Datos recibidos: {data.decode()}")

finally:
  # Por ultimo siempre debemos cerrar la conexions
  sock.close()
