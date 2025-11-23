# necesitamos importar el archivo .csv 
import csv
# necesitamos importar el archivo json 
import json
# from .helpers import get_file_path
# y declarar la ruta al mismo 
# necesitamos pasar la ruta relativa a absoluta para que ubique el archivo 
from pathlib import Path

# función que recibe el archivo a leer 
def get_login_csv(csv_file="data_login.csv"):
    csv_file = Path(__file__).parent.parent / "data" / csv_file
    # declaramos una variable que almacene una lista de clave-valor 
    casos = []

    # renombramos la expresión como h
    with open(csv_file, newline="") as h:
        # le decimos que lea el file con el método DictReader de csv 
        # que recibe el archivo como parámetro 
        read = csv.DictReader(h)
        # iteramos la variable read para obtener los valores diccionario de cada fila
        # y separamos por clave-valor los elementos a testear 
        for i in read:
            username = i["username"]
            password = i["password"]
            # lo convertimos al boleano que el test espera, ya que ahora es un string 
            # el método lower convierte en minúscula el dato que viene del file 
            login_example= i["login_example"].lower() == "true" 
            # y le inyectamos los datos parseados a la lista casos 
            casos.append((username,password,login_example))

    # devolvemos la variable casos rellenada  
    return casos

# versión del test para json
# se comenta para correr solo el test de csv 
""" def get_login_json(json_file="data_login.json"):

    # current_file = os.path.dirname(__file__)
    # json_file = os.path.join(current_file,"..","data",json_file)
    # # ../data/data_login.json=> rel
    # json_file = os.path.abspath(json_file)
    json_file = Path(__file__).parent.parent / "data" / json_file


    casos = []

    with open(json_file) as j:
        # en el caso de json usamos el método load para recibir el archivo a leer
        datos = json.load(j)

        for i in datos:
            username= i["username"]
            password=i["password"]
            login_example= i["login_example"]
            casos.append((username, password,login_example))
    return casos """