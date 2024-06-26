from secrets import usuario, senha
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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

class ParPerfeitoBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def login(self):
        self.driver.get('https://www.parperfeito.com.br/')
        self.driver.implicitly_wait(10)  # Aguarde até 10 segundos por qualquer elemento a ser encontrado
        print(self.driver.page_source)  # Exibir HTML da página no console para debug
        email_in = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        sleep(2)

        # Aceitar cookies
        cookie_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        cookie_btn.click()

        sleep(2)

        # Clicar no botão de login com Facebook
        fb_btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div/button/span')
        fb_btn.click()

        email_in = self.driver.find_element(By.XPATH, '//input[@name="email"]')
        email_in.send_keys(usuario)

        pw_in = self.driver.find_element(By.ID, 'password')
        pw_in.send_keys(senha)

        # Clicar no botão de login
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/form/div/div[1]/div[5]/button/span')
        login_btn.click()

        sleep(15)

    def like(self):
        # Esperar até que o botão de curtir seja visível
        self.driver.implicitly_wait(10)  # Aguarde até 10 segundos por qualquer elemento a ser encontrado
        print(self.driver.page_source)
        like_btn_locator = (By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/span/button/span/div[2]')
        like_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(like_btn_locator)
        )
        like_btn.click()

    def like2(self):
        # Clicar no segundo botão de curtir
        like_btn2 = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/span/button')
        like_btn2.click()

    def dislike(self):
        # Clicar no botão de descurtir
        dislike_btn = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[2]/button/span/span[2]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.like2()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()

    def close_popup(self):
        # Clicar no botão para fechar o popup
        popup_3 = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div/div[2]/div/button')
        popup_3.click()

    def close_match(self):
        # Clicar no botão para fechar a janela de match
        match_popup = self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/div/div[2]/div/button')
        match_popup.click()

bot = ParPerfeitoBot()
bot.login()


bot.auto_swipe()
