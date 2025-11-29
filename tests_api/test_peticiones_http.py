# importamos la librería requests y pytest para los tests
import requests
import pytest
# import pytest_check as check 
from faker import Faker
from datetime import datetime
from conftest import logger


fake = Faker()

def validate_api_response(response, expected_status,expected_fields=None, max_time=1.0):
    """Función helper para validar respuestas API con los 5 niveles"""
    # Nivel 1: Status
    assert response.status_code == expected_status
    # Nivel 2: Headers
    if expected_status != 204: # 204 No Content puede no tener Content-Type
        assert 'application/json' in response.headers.get('Content-Type', '')
    # Nivel 3-4: Estructura y contenido (si hay expected_fields)
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
        data = validate_api_response(
            response= respose,
            expected_status=200,
            expected_fields=[],
            max_time=2.0
        )


    @pytest.mark.get
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + "users")
        data = response.json() #LISTA   


        assert len(data) > 0
        assert isinstance(data,list)

        first_user = data[0]
        print(first_user)
        key_structure = ["id","name","username","phone","address","website"]

        for i in key_structure:
            assert i in first_user , f"campo {i} , no esta en {first_user}"


class TestPostUser:

    @pytest.mark.post
    def test_post_response_code(self,api_url):

        new_user = {
            "name":fake.name(),
            "email":fake.email(),
            "phone":fake.phone_number(),
            # "createdAt" :"2022-05-05"     
        }


        response = requests.post(api_url + "users", new_user)
        assert response.status_code == 201

        data = response.json()
        print(data)
        assert "id" in data

        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year  = datetime.now().year
            assert str(current_year) in created_at , f"no esta en el año"




class TestUserWorkflow:

    def test_completo_users(self, api_url):
        logger.info("TEST ENCANDENADOS : GET, POST , PUT , PATCH , DELETE")
        logger.info("1.GET Obtener usuarios")
        #GET: OBTENER LOS USUARIOS
        respose = requests.get(api_url + "users")
        data  = respose.json()
        check.equal(respose.status_code,200)
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
