# aquí desarrollamos el sistema de login con Selenium 
# importamos la librería que permite controlar el navegador
from selenium import webdriver
# importamos el By para mediante el findElement encontrar el tipo de selector 
from selenium.webdriver.common.by import By
# opciones para configurar el navegador de pruebas
from selenium.webdriver.chrome.options import Options
# importamos la versión del ChromeDriver correspondiente a nuestro navegador 
from webdriver_manager.chrome import ChromeDriverManager
# inicializar la instancia del servicio del driver 
from selenium.webdriver.chrome.service import Service
# importamos la librería para las esperas 
import time

# website a testear 
URL = 'https://www.saucedemo.com/'
# user para login 
USERNAME = 'standard_user'
# pass para login 
PASSWORD = 'secret_sauce'

''' 
función para instalación automática del driver y pasarle los servicios para iniciar 
el navegador y la sesión con Selenium
'''
def get_driver(): 
    # guardamos en una variable las opciones de configuración 
    # options  = Options()
    # le decimos que el navegador se inicie en tamaño maximizado 
    # options.add_argument('--start-maximized')

    # instalacion del driver
    service = Service(ChromeDriverManager().install())
    # creamos una instancia del driver y le pasamos los servicios para manejar el driver 
    driver = webdriver.Chrome(service=service)
    # le damos 5 segundos de espera para visualizar navegador antes de cerrar sesión 
    time.sleep(5)
    # la función retorna el driver 
    return driver

# a esta función le pasamos el driver para que pueda abrir la url en el navegador
def login_saucedemo(driver):
    # llamamos a la url deseada 
    driver.get(URL)
    
    # ingresar las credenciales 
    # usamos el find_element para encontrar los elementos buscados 
    # y en la función By le indicamos el tipo de selector a buscar 
    # el método send_keys nos permite tipear el texto 
    driver.find_element(By.NAME,'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME,'password').send_keys(PASSWORD)
    # sobre el botón usamos el método click() 
    driver.find_element(By.ID,'login-button').click()
    
    time.sleep(7)



