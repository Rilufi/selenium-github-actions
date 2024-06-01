from secrets import usuario, senha
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

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

    def login(self):
        self.driver.get('https://cp.ravenro.com.br/')
        sleep(2)
        email_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/input[1]')
        email_in.send_keys(usuario)
        pw_in = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/input[2]')
        pw_in.send_keys(senha)
        login_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/button[1]')
        login_btn.click()
        sleep(5)

    def tasker(self):
        self.driver.get('https://cp.ravenro.com.br/votar')
        task_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[5]/div[1]/div/div[2]/div[2]/button')
        task_btn.click()
        sleep(2)
        extend_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[5]/div[2]/div/div[2]/div[2]/button')
        extend_btn.click()
        sleep(2)

bot = TaskerBot()
bot.login()
bot.tasker()
