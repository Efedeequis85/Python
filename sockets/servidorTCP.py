import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 60000)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
  clienteSocket, clienteDir = server_socket.accept()
  try:
    while True:
    data = clienteSocket.recv(1024)


      if not data:
        break
        
      print(f"Datos: {data.decode()}")
      client_socket.sendall(b"Datos recibidos: " + data)
  finally:
  
    clienteSocket.close()
