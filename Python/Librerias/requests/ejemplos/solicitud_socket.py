import socket

# Definir los detalles de la solicitud
host = 'api/v2/pokemon/ditto'
port = 80
path = 'https://pokeapi.co/'

# Crear un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
sock.connect((host, port))

# Enviar la solicitud HTTP
request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
sock.sendall(request.encode())

# Recibir la respuesta
response = b''
while True:
    data = sock.recv(4096)
    if not data:
        break
    response += data

# Cerrar la conexión
sock.close()

# Imprimir la respuesta
print(response.decode())
