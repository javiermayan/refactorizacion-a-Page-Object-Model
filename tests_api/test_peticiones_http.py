# importamos la librería requests y pytest para los tests
import requests
import pytest
# importamos la librería check para aserción blanda sin romper ejecución
import pytest_check as check 
# importamos Faker para generar datos aleatorios para test de POST
from faker import Faker
# importamos un módulo de Python para obtener la fecha y validar en POST
from datetime import datetime
# importamos la función looger() para obtener info de las ejecuciones 
from conftest import logger

# instanciamos Faker
fake = Faker()

# Función helper para validar respuestas API con los 5 niveles 
def validate_api_response(response, expected_status,expected_fields=None, max_time=1.0):    
    # Nivel 1: Status = status code esperado
    assert response.status_code == expected_status
    # Nivel 2: Headers: los Headers esperados, 204 = no tiene contenido 
    if expected_status != 204: # 204 No Content puede no tener Content-Type
        # esperamos json 
        assert 'application/json' in response.headers.get('Content-Type', '')
    # Nivel 3-4: Estructura y contenido (si hay expected_fields)
    # los campos esperados en la estructura de la respuesta 
    if expected_fields and response.text:
        body = response.json()
        assert expected_fields <= set(body.keys())
    # Nivel 5: Performance
    assert response.elapsed.total_seconds() < max_time
    return response.json() if response.text else {}

# creamos una clase donde uso los makers del método GET 
class TestGetUser:

    @pytest.mark.get
    # creamos la función test iniciando el nombre con test_
    # test para validar el status code recibido 
    # en parámetros hacemos referencia a la clase misma y al fixture que usaremos
    def test_get_response_code(self, api_url):
        # hacemos las peticiones 
        # en variable respose guardamos la respuesta del método get()
        # le pasamos la url + el endpoint a consumir 
        respose = requests.get(api_url + "users")
        # llamamos a la función validate_api_response de validación genérica (Helper)
        data = validate_api_response(
            response= respose,
            expected_status= 200,
            expected_fields= [],
            max_time= 2.0
        )
        # la misma validación, sin usar la función Helper anterior
        assert respose.status_code == 200


    # creamos otro marker para get pero ahora para testear la data
    # aunque podrían estar ambas pruebas dentro de un mismo marker
    @pytest.mark.get
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + "users")
        # almacenamos la response en formato json 
        data = response.json() # se presenta una estructura del tipo LISTA   

        # validamos que tenga data 
        assert len(data) > 0
        # validamos la estrutura del tipo list
        # primer parámetro: la info a validar, y el 2do: el tipo de estructura a comparar
        assert isinstance(data, list)

        # obtenemos la estructura de la respuesta para conocer los campos que contiene 
        # buscamos el primer usuario de la lista recibida en data 
        first_user = data[0]
        print(first_user)
        # enumeramos los campos que esperamos en la respuesta 
        key_structure = ["id", "name", "username", "phone", "address", "website"]

        # en cada iteración i toma el valor de cada uno de los campos que llegan en la estructura 
        for i in key_structure:
            # validamos que el campo exista en la response 
            assert i in first_user , f"campo {i} , no está en {first_user}"

# creamos una clase donde uso los makers del método POST 
class TestPostUser:

    @pytest.mark.post
    def test_post_response_code(self,api_url):

        # creamos la variable que representa el nuevo usuario a crear 
        # en este caso es un diccionario y usamos faker para rellenar los campos
        new_user = {
            "name":fake.name(),
            "email":fake.email(),
            "phone":fake.phone_number(),
            # hardcodeamos la fecha de creación del usuario 
            # dejamos comentado createdAt para no fallar el test 
            # "createdAt" :"2022-05-05"     
        }


        response = requests.post(api_url + "users", new_user)
        # validamos el status code esperado, en este caso un 201
        assert response.status_code == 201

        data = response.json()
        # creamos un print para visualizar la respuesta 
        print(data)
        # validamos la creación del campo id 
        assert "id" in data

        # validamos si el año de creación del dato es el esperado 
        if "createdAt" in data:
            # si existe en data el campo createdAt lo almacenamos en la nueva variable created_at
            created_at = data["createdAt"]
            # capturamos en una variable el año actual 
            current_year  = datetime.now().year
            # current_year viene como tipo de dato fecha 
            # lo convertimos a string para hacer la validación 
            # en el caso de no encontrarse se visualiza el mensaje de 2do parámetro 
            assert str(current_year) in created_at, f"no esta en el año"

# creamos una clase que nos permita poner todo en un mismo test 
# transfiriendo la lógica de los tests anteriores
class TestUserWorkflow:

    # definimos la estructura del test 
    def test_completo_users(self, api_url):
        # llamamos a la función que escribe en el log eventos de la ejecución del test
        logger.info("TEST ENCANDENADOS : GET, POST, PUT, PATCH, DELETE")
        logger.info("1.GET Obtener usuarios")
        #GET: OBTENER LOS USUARIOS
        respose = requests.get(api_url + "users")
        data  = respose.json()
        # acá en lugar del assert usamos el check para no interrumpir ejecución si falla
        # para eso usamos el método equal del check comparando lo recibido con lo esperado
        check.equal(respose.status_code, 200)
        # método de check para validar booleanos 
        check.is_true(len(data) > 0)

        print("1.POST crear usuarios") # esto no se visualiza
        
        new_user = {
            "name":fake.name(),
            "email":fake.email(),
            "phone":fake.phone_number(),
            # "createdAt" :"2022-05-05"     
        }


        response = requests.post(api_url + "users", new_user)
        assert response.status_code == 201
