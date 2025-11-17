import pytest 
# importamos By para capturar los elementos 
from selenium.webdriver.common.by import By
import sys
import os
# esto nos permite obtener la ruta del archivo actual con esta estructura de carpetas
# convierte la ruta relativa en absoluta 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
# importamos las funciones para llamar al driver y acceder al login 
from utils.helpers import get_driver, login_saucedemo


# scope='session' nos permite ejecutar todos los tests sin cerrar la sesión en curso
# @pytest.fixture(scope='session') 
@pytest.fixture # de esta manera ejecuta test por test con su propia sesión 
def driver():
	# configuracion para consultar a Selenium webdriver 
    # llamamos a la función get_driver() y la almacenamos en una variable 
    driver = get_driver()
    # le entrega al navegador el driver 
    yield driver
    # finalida la sesión del driver lo cerramos 
    driver.quit()

# le pasamos el driver al login 	
def test_login(driver):
    # llamamos a la funcion login_saucedemo de helpers y le pasamos el driver 
    login_saucedemo(driver)
	# assert para el valor del input para validar credenciales 
	# click al botón de login
    # validamos que accedimos al inventario con el método current_url del driver 
    assert "/inventory.html" in driver.current_url
    # verificar elementos importantes de la página 
    # validamos el título de la página del inventario 
    # lo capturamos por su class name usando la clase del span y del div que lo contiene 
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'

def test_catalogo(driver):
	# iniciar login 
    login_saucedemo(driver)
    # buscamos la presencia de la clase inventory_item para asegurar que hay productos
    # usamos find_elements para buscar dentro de una lista de elementos similares
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # validamos, si products es mayor que cero, existen item listados 
    assert len(products) > 0	  

# test para validar el acceso al carrito de compras 
# le pasamos el driver para inciar otra sesión 
def test_carrito(driver):
    # repetimos los pasos del test de catálogo 
    login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0	
    # hacemos una captura de imagen como evidencia 
    driver.save_screenshot('inventario.png')
    # agregamos un producto al carrito 
    # buscamos el primer elemento de la lista de productos y le hacemos click 
    products[0].find_element(By.TAG_NAME, 'button').click()
	# ir al carrito de compras 
	# verificar que carrito se incremente clase del elemento span 
	# verificar que en el carrito aparezca el producto 
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"  
