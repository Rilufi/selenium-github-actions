import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from time import sleep

# Lista de credenciais
credenciais = [
    {"usuario": os.getenv("USUARIO"), "senha": os.getenv("SENHA")},
    {"usuario": os.getenv("USUARIO2"), "senha": os.getenv("SENHA")},
    {"usuario": os.getenv("USUARIO3"), "senha": os.getenv("SENHA")},
    {"usuario": os.getenv("USUARIO_TULYO"), "senha": os.getenv("SENHA_TULYO")}
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
        self.driver.get('https://cp.ravenro.com.br/')
        sleep(2)
        try:
            email_in = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Login"]')))
            email_in.send_keys(usuario)
            pw_in = self.driver.find_element(By.XPATH, '//input[@placeholder="Senha"]')
            pw_in.send_keys(senha)
            login_btn = self.driver.find_element(By.XPATH, '//button[contains(@class, "baTaHaVg0")]')
            login_btn.click()
            sleep(5)
        except TimeoutException as e:
            print(f"Erro ao localizar elementos de login: {e}")

    def voter1(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(5)
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="clickable-element bubble-element Button baTaHxaE"]')))
            btn.click()
            sleep(2)
        except (TimeoutException, NoSuchElementException):
            time_elements = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Aguarde:") and contains(@class, "bubble-element Text")]')
            for element in time_elements:
                print(f"Tempo restante para votar: {element.text}")
            sleep(2)

    def voter2(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(5)
        try:
            btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="clickable-element bubble-element Button baTaIaCh"]')))
            btn.click()
            sleep(2)
        except (TimeoutException, NoSuchElementException):
            time_elements = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Aguarde:") and contains(@class, "bubble-element Text")]')
            for element in time_elements:
                print(f"Tempo restante para votar: {element.text}")
            sleep(2)

    def logoff(self):
        self.driver.get('https://cp.ravenro.com.br/inicio')
        try:
            logoff_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "logoff-btn")]')))
            logoff_btn.click()
        except TimeoutException as e:
            print(f"Erro ao tentar fazer logoff: {e}")
        finally:
            self.driver.quit()

for cred in credenciais:
    if not cred["usuario"] or not cred["senha"]:
        raise ValueError("Usuário ou senha não foram configurados corretamente nos segredos do ambiente.")

    bot = TaskerBot()
    bot.login(cred["usuario"], cred["senha"])
    bot.voter1()
    bot.voter2()
    bot.logoff()
