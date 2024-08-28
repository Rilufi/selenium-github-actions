import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep


# Lista de credenciais
credenciais = [
    {"usuario": os.getenv("USUARIO_TALES"), "senha": os.getenv("SENHA_TALES")}
]

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

class TaskerBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 15)

    def login(self, usuario, senha):
        print(f"{usuario} votando")
        self.driver.get('https://ragnatales.com.br/profile/login')
        sleep(2)
        try:
            email_in = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Endereço de E-mail"]')))
            email_in.send_keys(usuario)
            pw_in = self.driver.find_element(By.XPATH, '//input[@placeholder="Digite sua senha de acesso"]')
            pw_in.send_keys(senha)
            pw_in.send_keys(Keys.ENTER)
#            login_btn = self.driver.find_element(By.XPATH, '//button[contains(@class, "baTaHaVg0")]')
 #           login_btn.click()
            sleep(5)
        except TimeoutException as e:
            print(f"Erro ao localizar elementos de login: {e}")

    def votar(self, botao_xpath):
        self.driver.get('https://ragnatales.com.br/profile/vote')
        sleep(5)
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, botao_xpath)))
            btn.click()
            print("Votado!")
            sleep(2)
        except (TimeoutException, NoSuchElementException):
            time_elements = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Aguarde:") and contains(@class, "bubble-element Text")]')
            if time_elements:
                print(f"Tempo restante para votar: {time_elements[0].text}")
            sleep(2)
        except UnexpectedAlertPresentException:
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
                print("Alerta inesperado resolvido em votar.")
            except NoAlertPresentException:
                print("Nenhum alerta presente para resolver.")

    def quiter(self):
        self.driver.quit()


for cred in credenciais:
    if not cred["usuario"] or not cred["senha"]:
        raise ValueError("Usuário ou senha não foram configurados corretamente nos segredos do ambiente.")
    
    print(f"Iniciando votação para {cred['usuario']}")
    bot = TaskerBot()
    try:
        bot.login(cred["usuario"], cred["senha"])
        bot.votar('//button[contains(@class, "rounded-xl") and contains(@class, "bg-primary") and text()[contains(., "Votar")]]'
)  # Primeiro botão
#        bot.votar('//button[@class="clickable-element bubble-element Button baTaIaCh"]')  # Segundo botão
    except Exception as e:
        print(f"Erro durante a execução para {cred['usuario']}: {e}")
    finally:
        bot.quiter()
    print(f"Finalizado para {cred['usuario']}")
