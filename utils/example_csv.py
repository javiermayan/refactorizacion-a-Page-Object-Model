# necesitamos importar el archivo .csv 
import csv
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