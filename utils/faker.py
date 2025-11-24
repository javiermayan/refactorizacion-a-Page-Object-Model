# importamos librería Faker para crear datos falsos aleatorios pero realistas 
from faker import Faker

# lo instanciamos para usar los métodos de creación de datos 
fake = Faker() 

# creamos una función para luego invocarla desde los tests 
# y le pasamos el nro de casos aleatorios que queremos que evalúe
def get_login_faker(num_casos=5):
    # declaramos un lista vacía 
    casos = []
    # los casos de faker van a fallar todos porque está intentando con credenciales no válidas
    # tenemos que mezclar casos positivos harcodeados con aleatorios desde Faker 
    usuarios_validos = ["standard_user", "locked_out_user"]
    # password_valido = "secret_sauce"

    # no necesitamos conocer el valor de la variable y ponemos un guión bajo en su lugar
    # lo hacemos iterar hasta 5 que es el num_casos
    # y le pedimos que genere los 3 tipos de datos que necesitamos 
    for _ in range(num_casos):
        # llamamos a los métodos de Faker que correspondan al dato a crear 
        username = fake.user_name() 
        # le asignamos un largo de 12 caracteres a la contraseña 
        password = fake.password(length=12) 
        # chance_of_getting_true es la probabilidad de TRUE en los casos generados
        login_example = fake.boolean(chance_of_getting_true=50) 
        # inyectamos casos positivos harcodeados cuando login_example sea TRUE
        if login_example == True:
            username = "standard_user"
            # también podemos seleccionar el usuario aleatoriamente desde una lista
            # username = fake.random.choice(usuarios_validos)
            password = "secret_sauce"
        
        # le inyectamos los valores a la lista casos 
        casos.append((username, password, login_example))
    
    # retornamos los casos al parametrize para que sepa cuantos evaluar 
    return casos