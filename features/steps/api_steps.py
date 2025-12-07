# este archivo realiza todo lo escrito en .feature 
# indica el cómo lo hacemos 
# nos importamos de la librería behave 3 palabras claves de Gherkin
from behave import when, then, given
# importamos la librería para poder hacer las peticiones
import requests

# indicamos en una variable la URL donde están los endpoints a probar 
BASE_URL = "https://jsonplaceholder.typicode.com"

# comprobar si la API está disponible 
# invocamos al módulo respectivo de Behave 
@given('la API está disponible')
# este módulo ejecuta la siguiente función para validar que esté activa la API
# la variable context es la que se transfiere y comunica paso del proceso 
def step_api_available(context):
    # creamos un método para que almacene la URL 
    context.base_url = BASE_URL

# indicamos cómo hacer el paso previo
# endpoint representa el complemento de la URL base
# se obtiene desde el When del archivo .feature 
@when('hago GET a "{endpoint}"')
def step_get_request(context, endpoint):
    context.response = requests.get(f"{context.base_url}{endpoint}")

@when('hago POST a "{endpoint}" con:')
def step_post_with_table(context, endpoint):
    # Convertir tabla a diccionario
    data = {}
    for row in context.table:
        data[row[0]] = row[1]
    
    context.response = requests.post(f"{context.base_url}{endpoint}", json=data)

@then('el status debe ser {status:d}')
def step_check_status(context, status):
    assert context.response.status_code == status