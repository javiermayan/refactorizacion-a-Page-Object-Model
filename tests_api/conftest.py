# aquí van todos los fixtures que necesite 

import pytest
import logging
import pathlib

# fixture de la url donde hacer las peticiones en lugar del archivo main.py anterior
@pytest.fixture
def api_url():
    return 'https://jsonplaceholder.typicode.com/'



# def pytest_html_summers(prefix):

#     prefix.extend([
#         '<h2>MISION IM CUMPLIDA</h2>',
#         '<div style="background:gold"></div>'
#     ])


path_dir = pathlib.Path('logs')
path_dir.mkdir(exist_ok=True)


logging.basicConfig(
    filename= path_dir/ "historial.log",
    level= logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s – %(message)s',
    datefmt='%H:%M:%S'
)

logger = logging.getLogger()
