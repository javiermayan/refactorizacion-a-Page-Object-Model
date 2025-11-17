
# importamos la url y credenciales desde helpers 
from utils.helpers import URL, USERNAME, PASSWORD
from selenium.webdriver.common.by import By
# también importamos WebDriverException y EC para las esperas explícitas 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage: 	
    # declaramos los atributos de los elementos de la page a capturar para luego asignarle los valores importados 
    _INPUT_NAME = (By.NAME, 'user-name')
    _INPUT_PASSWORD = (By.NAME, 'password')
    _LOGIN_BUTTON = (By.NAME, 'login-button')
	
    def __init__(self,driver):
    # cuando inicializa el login también inicializa el drive 
        self.driver = driver 
		
    # necesito 2 métodos para abrir la url 
    # 1- llama al driver y obtiene la url a
    def open(self):
    # abrir la url 
        self.driver.get(URL)
		
    # 2- tipear el user y pass y le asignamos el valor importado 
    def login(self, username= USERNAME, password = PASSWORD): 
    # ejecutamos un espera explícita para asegurar que el elemento se haya cargado
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)

        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)
	
        # una vez que completa credenciales, debe pulsar el botón 
        WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()