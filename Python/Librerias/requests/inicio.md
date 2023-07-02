### Antes de empezar a trabajar con requests:

* verificar si tenés instalada la libreria en tu entorno de Python, podes hacerlo desde el interprete 
de Python:

**import requests**

print("Versión de Requests:", requests.__version__)

* si no está instalada, podés instalarla con el siguiente comando, o en caso de que si esté 
instalada pero querrás actualizarla:

**pip install --upgrade requests**

* **hacer una solicitud http:**

response = requests.get('https://api.github.com/events')
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
response = requests.put('https://httpbin.org/put', data={'key': 'value'})
response = requests.delete('https://httpbin.org/delete')
response = requests.head('https://httpbin.org/get')
response = requests.options('https://httpbin.org/get')

* Pasar parámetros en la URL:

A veces necesitamos enviar datos en la URL, si se hiciera en forma manual deberíamos pasar estos 
datos como pares clave/valor después de un signo de interrogación:

    http://example.com/path?param1=value1&param2=value2

Pero con requests se pueden enviar parametros de forma muy simple, como un diccionario, usando el
argumento "params":

    payload = {'key1': 'value1', 'key2': 'value2'}
    response = requests.get('https://httpbin.org/get', params=payload)

Podemos verificar si se ha codificado correctamente la url esperada con un print(response.url)

No se pueden agregar claves cuyo valor sea None.
Si se pueden agregar listas como valores, por ejemplo:

    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

    response = requests.get('https://httpbin.org/get', params=payload)
    print(r.url)
    https://httpbin.org/get?key1=value1&key2=value2&key2=value3

__Atributos más usados de la clase Response:__

    - status_code: Código de estado de la respuesta HTTP.
    - headers: Diccionario que contiene los encabezados de la respuesta.
    - text: Contenido de la respuesta como una cadena de texto Unicode.
    - encoding: Esquema de codificación utilizado para decodificar el contenido de la respuesta.
     Se puede verificar la codificación --> r.encoding
                                            'utf-8'
     y cambiar a otra --> r.encoding = 'ISO-8859-1'
    - content: si se determina el tipo de codificación en el doc HTML o XML, debemos usar --> 
    r.content para encontrar la codificación y luego poder cambiarla, en caso de ser necesario con    r.encoding
       
__Métodos de la clase Response:__

    json(): Devuelve el contenido de la respuesta interpretado como JSON.
    raise_for_status(): Lanza una excepción si la respuesta tiene un código de estado de error.
    iter_content(): Itera sobre el contenido de la respuesta en bloques.
    iter_lines(): Itera sobre las líneas del contenido de la respuesta.

__Argumentos de la función requests:__

    url: La URL a la que se realiza la solicitud.
    method: El método de la solicitud HTTP (por defecto es GET).
    params: Parámetros que se envían en la URL de la solicitud.
    data: Datos que se envían en el cuerpo de la solicitud.
    headers: Encabezados que se incluyen en la solicitud HTTP.
    auth: Objeto de autenticación para autenticarse en el servidor.
    timeout: Tiempo máximo de espera para la respuesta del servidor.
    verify: Especifica si se verifica o no el certificado SSL del servidor.
