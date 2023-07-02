import http.client

# Establecer los detalles de la solicitud
host = 'https://pokeapi.co/api/v2/pokemon/ditto'
path = '/'

# Crear una conexión HTTP
conn = http.client.HTTPConnection(host)

# Enviar la solicitud GET
conn.request('GET', path)

# Obtener la respuesta
response = conn.getresponse()

# Leer el contenido de la respuesta
data = response.read()

# Imprimir la respuesta
print(data.decode())

# Cerrar la conexión
conn.close()
