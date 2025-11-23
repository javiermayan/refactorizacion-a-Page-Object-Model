import pytest
# importamos la clase page
from page.login_page import LoginPage
# imortamos el archivo de datos 
from data.data_login import CASOS_LOGIN 
# para csv ya no necesitamos importar CASOS_LOGIN 
# debemos importar la función get_login_csv desde example_csv
# y get_login_json desde data_login.json 
from utils.example_csv import get_login_csv
# from utils.example_csv import get_login_json


# parametrizamos los distintos usuarios
#@pytest.mark.parametrize("username,password,login_bool",CASOS_LOGIN)
# para csv no pasamos los casos del archivo sino la función correspondiente get_login_csv
@pytest.mark.parametrize("username, password, login_bool", get_login_csv())
# para json le pasamos su función get_login_csv
#@pytest.mark.parametrize("username, password, login_bool", get_login_json())
# declaramos el test e inicializamos el driver 
def test_login(driver, username, password, login_bool):
    # creamos el objeto (instanciarlo) 
    loginPage = LoginPage(driver) 
	# y le permite al objeto creado los métodos de la clase 
	# abrimos la página 
    loginPage.open()
    # le pasamos el username, password al login para evaluar credenciales
    loginPage.login(username, password)

    # probamos el booleano de las credenciales 
    if login_bool:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url
