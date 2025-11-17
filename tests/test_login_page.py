import pytest
# importamos la clase page
from page.login_page import LoginPage

# declaramos el test e inicializamos el driver 
def test_login(driver):
    # creamos el objeto (instanciarlo) 
    loginPage = LoginPage(driver) 
	# y le permite al objeto creado los métodos de la clase 
	# abrimos la página 
    loginPage.open()
    loginPage.login()
