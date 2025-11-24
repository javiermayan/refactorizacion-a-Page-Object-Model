# TEST PARA API / REST

"""
    API => ( APPLICATION PROGRAMMING INTERFACE)

    GET => obetner datos
    POST => envio de datos => creacion de datos / login
    PUT  => edicion de datos totales => todos 
    PATCH  => edicion de datos parciales => username 
    DELETE => eliminar datos

    pip install requests

    1xx=> informacion
    2xx => exito
        201 => creacion
    3xx => comunicacion / redireccion 
    4xx => casos de error de cliente => frontend interface
    5xx=> sever falla => errores de srevidor

    CRUD 
"""

import requests

URL_API = "https://jsonplaceholder.typicode.com/"

# función para obtener los usuarios de la web jsonplaceholder
def get_users():
    # mensaje de procesamiento
    print("OBTENIENDO USERS...")
    # almacenamos en una variable la petición que hace el método get()
    # el endpoint a pegarle es https://jsonplaceholder.typicode.com/users
    response = requests.get(URL_API + "users")

    # imprimimos el status code de la respuesta obtenida 
    print(response.status_code)

    # esperamos que el status code de éxito sea = 200 
    assert response.status_code == 200

    # si pusiéramos un 201 fallaría el assert 
    # assert response.status_code == 201

    # almacenamos la response en la variable data en formato json 
    data = response.json()
    # imprimimos el contenido de la respuesta 
    print(data)

# creamos un usuario nuevo 
def post_users():
    # mensaje de procesamiento
    print('CREANDO USUARIOS')

    # creamos una variable que almacene un diccionario con los datos del nuevo user 
    new_user = {
        "name":"Nati",
        "email" : "",
        "phone": "22323232323"
    }

    # almacenamos la response en la variable response
    # el método post necesita la url y un json con los datos a enviar 
    response = requests.post(URL_API + "users", new_user)
    # visualizamos la respuesta del status code que esperamos un 201 en este caso
    print(response.status_code)
    # almacenamos la respuesta en json 
    data = response.json()
    # el nro de id que devuelve es el id agregado a los que ya están 
    print(data)

# reemplaza o elimina los datos del usuario 
def put_user():
    print("actualizando total de usuario...")
    
    # datos y id del usuario que queremos actualizar
    user_update = {
        "id":1,
        "name": "hola mundo"
    }

    # le tenemos que indicar el id del registro a modificar 
    response = requests.put(URL_API + "users/1", user_update)
    print(response.status_code)

# modifica solo algunos campos del usuario 
def patch_user():
    print("actualización parcial del usuario...")
    
    user_update = {
        "id":1,
        "email":"asasa@gmail.com"
    }

    response = requests.patch(URL_API + "users/1", user_update)
    # en este caso devuelve un 200 
    print(response.status_code)

# elimina usuario con id indicado 
def delete_user():
    print("eliminando usuario indicado...")

    response = requests.delete(URL_API + "users/1")
    print(response.status_code)


# get_users()
# post_users()
# put_user()
# patch_user()
delete_user()