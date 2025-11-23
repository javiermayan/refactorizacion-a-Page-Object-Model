import pytest
# importamos la clase page
from page.login_page import LoginPage
# imortamos el archivo de datos 
from data.data_login import CASOS_LOGIN 

# parametrizamos los distintos usuarios
@pytest.mark.parametrize("username,password,login_bool",CASOS_LOGIN)
# declaramos el test e inicializamos el driver 
def test_login(driver, username, password, login_bool):
    # creamos el objeto (instanciarlo) 
    loginPage = LoginPage(driver) 
	# y le permite al objeto creado los métodos de la clase 
	# abrimos la página 
    loginPage.open()
    # le pasamos el username, password al login para evaluar credenciales
    loginPage.login(username, password)
