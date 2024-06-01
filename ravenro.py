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

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
#   "--headless",
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

    def login(self):
        self.driver.get('https://cp.ravenro.com.br/')
        sleep(2)
#        fb_btn = self.driver.find_element(By.CLASS_NAME,'login_link')
 #       fb_btn.click()
        email_in = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/input[1]')
        email_in.send_keys(usuario)
        pw_in = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/input[2]')
        pw_in.send_keys(senha)
        login_btn = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/button[1]')
        login_btn.click()
        sleep(5)

    def tasker(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        task_btn = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div/div[2]/div[2]/button')
        task_btn.click()
        sleep(2)
        extend_btn = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[5]/div[2]/div/div[2]/div[2]/button')
        extend_btn.click()
        sleep(2)

bot = TaskerBot()
bot.login()
bot.tasker()
