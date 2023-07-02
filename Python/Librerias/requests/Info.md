Requests

Es una herramienta para hacer consultas HTTP de forma simple con Python.
Cuenta con una interfaz (conjunto de métodos y funciones ) para interactuar con el protocolo HTTP de manera sencilla, sin tener que hacerlo de forma manual o mediante sockets.
Incluye métodos como get(), post(), put(), delete(), entre otros para realizar solicitudes HTTP específicas, como:
 obtener datos de un servidor, 
enviar datos a través de una solicitud POST, 
actualizar recursos mediante una solicitud PUT 
eliminar recursos mediante una solicitud DELETE. 


Solo necesitas llamar al método adecuado y proporcionar los parámetros necesarios ( URL, encabezados, los datos y otros detalles de la solicitud.)
Es muy útil para interactuar con APIs, realizar scraping web y realizar solicitudes HTTP en general.

Nos permite:
realizar solicitudes 
Manejar respuestas
Trabajar con datos relacionados a HTTP 
incluir parametros, encabezados personalizados, datos de formularios, archivos adjuntos, etc
Maneja automaticamente la administración de conexiones, redirecciones, cookies, etc
Otras características:
autenticación, 
manejo de sesiones, 
verificación SSL, 
manejo de redirecciones

Ejemplo básico de como usar la libreria requests:

import requests

response = requests.get('https://api.example.com')
print(response.status_code)  # Imprime el código de estado de la respuesta
print(response.text)  # Imprime el contenido de la respuesta en formato de texto


