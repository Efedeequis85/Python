import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server.connect(server_address)
solicitud = "SOLUCITUD"

try:
  server.sendall(message.encode())
  data = client_socket.recv(1024)
  
  print(f"Datos recibidos: {data.decode()}")
finally:
  sock.close()
