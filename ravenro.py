import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException, NoAlertPresentException, NoSuchElementException
from time import sleep

# Lista de credenciais
credenciais = [
    {"usuario": os.getenv("USUARIO"), "senha": os.getenv("SENHA")},
    {"usuario": os.getenv("USUARIO2"), "senha": os.getenv("SENHA")},
    {"usuario": os.getenv("USUARIO_TULYO"), "senha": os.getenv("SENHA_TULYO")}
]

chrome_service = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

class TaskerBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)  # 10 segundos de espera explícita

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Alerta presente: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            pass

    def login(self, usuario, senha):
        self.driver.get('https://cp.ravenro.com.br/')
        sleep(2)
        email_in = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/input[1]')))
        email_in.send_keys(usuario)
        pw_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/input[2]')
        pw_in.send_keys(senha)
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/button[1]')
        login_btn.click()
        sleep(5)

    def tasker(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        self.handle_alert()  # Verifica e lida com alertas antes de continuar
        try:
            task_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "baTaHxaE")]')))
            task_btn.click()
        except (TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException) as e:
            print(f"Erro ao clicar no primeiro botão de votação: {e}")
            self.handle_alert()
            try:
                # Lê o tempo restante
                time_element = self.driver.find_element(By.XPATH, '//div[@class="bubble-element Text baTaIaCt"]')
                print(f"Tempo restante para votar: {time_element.text}")
            except NoSuchElementException:
                print("Elemento de tempo restante não encontrado.")
        
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(2)
        self.handle_alert()  # Verifica e lida com alertas antes de continuar
        try:
            extend_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "baTaIaCh")]')))
            extend_btn.click()
        except (TimeoutException, ElementNotInteractableException, UnexpectedAlertPresentException) as e:
            print(f"Erro ao clicar no segundo botão de votação: {e}")
            self.handle_alert()
            try:
                # Lê o tempo restante
                time_element = self.driver.find_element(By.XPATH, '//div[@class="bubble-element Text baTaIaCt"]')
                print(f"Tempo restante para votar: {time_element.text}")
            except NoSuchElementException:
                print("Elemento de tempo restante não encontrado.")
        
        sleep(2)

    def close(self):
        logoff_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//text[@class="fa" and contains(text(), "")]')))
        logoff_btn.click()
        self.driver.quit()

for cred in credenciais:
    if not cred["usuario"] or not cred["senha"]:
        raise ValueError("Usuário ou senha não foram configurados corretamente nos segredos do ambiente.")
    
    bot = TaskerBot()
    bot.login(cred["usuario"], cred["senha"])
    bot.tasker()
    bot.close()
