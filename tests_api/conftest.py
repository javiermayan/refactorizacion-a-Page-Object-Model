# archivo donde van todos los fixtures que se necesiten 
# las fixtures preparan datos para ser consumidos por los tests

import pytest
# importamos librería que permite tener historial de ejecuciones en un archivo
import logging
# importamos librería para poder ubicar el archivo en su carpeta
import pathlib

# declaramos la fixture
@pytest.fixture
# fixture de la url donde hacer las peticiones en lugar del archivo main.py anterior
def api_url():
    return 'https://jsonplaceholder.typicode.com/'



# creamos una función para modificar el reporte html 
# def pytest_html_summers(prefix):

#     prefix.extend([
#         '<h2>MISION IM CUMPLIDA</h2>',
#         '<div style="background:gold"></div>'
#     ])


# creamos variable que almacena ubicación de la carpeta 
# y le indicamos el nombre de carpeta que crea en raíz de proyecto
path_dir = pathlib.Path('logs')
# validamos si existe la carpeta previamente 
path_dir.mkdir(exist_ok=True)

# configuración global para el logging mediante método basicConfig()
logging.basicConfig(
    # ruta donde se almacena archivo log con historial
    filename= path_dir/ "historial.log",
    # le asignamos un nivel de información INFO 
    level= logging.INFO,
    # el formato de información
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    # el formato de hora en el que se ejecutó el test 
    datefmt='%H:%M:%S'
)

# creamos una variable que almacene lo que queremos escribir de la ejecución 
# y nos permita luego usarla en un test 
logger = logging.getLogger()
