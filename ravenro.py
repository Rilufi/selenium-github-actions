import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")

if not usuario or not senha:
    raise ValueError("Usuário ou senha não foram configurados corretamente nos segredos do ambiente.")

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

    def login(self):
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
        try:
            task_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div/div[2]/div[2]/button')))
            task_btn.click()
        except TimeoutException:
            print("Primeiro botão de votação não encontrado, tentando o segundo.")
        
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(2)
        try:
            extend_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[5]/div[2]/div/div[2]/div[2]/button')))
            extend_btn.click()
        except TimeoutException:
            print("Segundo botão de votação não encontrado.")

        sleep(2)

bot = TaskerBot()
bot.login()
bot.tasker()
