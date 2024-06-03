import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.core.utils import ChromeType
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from datetime import datetime
from selenium.webdriver.common.by import By

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
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def login(self, usuario, senha):
        self.driver.get('https://cp.ravenro.com.br/')
        sleep(2)
        email_in = self.driver.find_element("xpath",'<input class="bubble-element Input baTaHaVb0 a1717435427938x967" type="input" placeholder="Login" style="background-color: rgb(255, 255, 255);">')
        email_in.send_keys(username)
        pw_in = self.driver.find_element("xpath",'<input class="bubble-element Input baTaHaVf0 a1717435427938x967" type="password" placeholder="Senha" autocomplete="new-password" style="background-color: rgb(255, 255, 255);">')
        pw_in.send_keys(password)
        login_btn = self.driver.find_element("xpath",'<button class="clickable-element bubble-element Button baTaHaVg0" style="box-shadow: 0px 7px 30px -10px rgba(var(--color_primary_default_rgb), 0.1); background: none rgb(228, 161, 1);">LOGIN</button>')
        login_btn.click()
        sleep(5)

    def voter1(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(5)
        try:
            task_btn = self.driver.find_element("xpath",'<button class="clickable-element bubble-element Button baTaHxaE" style="max-height: unset; box-shadow: rgba(68, 76, 231, 0.1) 0px 7px 30px -10px; background: none rgb(108, 127, 235); border-color: rgb(108, 127, 235);">Votar</button>')
            task_btn.click()
            sleep(2)
        except:
            remain_time = self.driver.find_element("xpath",'<div class="bubble-element Text baTaIaCt">')
            print(remain_time.text)
            sleep(2)

    def voter2(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        sleep(5)
        try:
            task_btn = self.driver.find_element("xpath",'<button class="clickable-element bubble-element Button baTaIaCh" style="max-height: unset; box-shadow: rgba(68, 76, 231, 0.1) 0px 7px 30px -10px; background: none rgb(108, 127, 235); border-color: rgb(108, 127, 235);">Votar</button>')
            task_btn.click()
            sleep(2)
        except:
            remain_time = self.driver.find_element("xpath",'<div class="bubble-element Text baTaIaCz">')
            print(remain_time.text)
            sleep(2)

    def logoff(self):
        # Voltar para a página inicial
        self.driver.get('https://cp.ravenro.com.br/inicio')
        try:
            logoff_btn = self.driver.find_element("xpath", '<text class="fa" x="50%" y="50%" text-anchor="middle" style="font-size: 50px; fill: currentcolor;"></text>')
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
