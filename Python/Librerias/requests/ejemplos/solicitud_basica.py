import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
# print(response.status_code)  # Imprime el código de estado de la respuesta
# print(response.text)  # Imprime el contenido de la respuesta en formato de texto

#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(f"status code: {r.status_code}")
print(f"headers: {r.headers}")
print(f"content-type: {r.headers['content-type']}")
print(f"encoding: {r.encoding}")
print(f"text: {r.text}")
print(f"json: {r.json()}")