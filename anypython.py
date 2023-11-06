from secrets import username, password
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

    def login(self):
        self.driver.get('https://www.pythonanywhere.com/')

#        sleep(2)

#        cookie = self.driver.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]')
#        cookie.click()

        sleep(2)

        fb_btn = self.driver.find_element("xpath",'/html/body/div[1]/nav[1]/div/ul/li[6]/a')
        fb_btn.click()

        email_in = self.driver.find_element("xpath",'//*[@id="id_auth-username"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element("xpath",'//*[@id="id_auth-password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element("xpath",'//*[@id="id_next"]')
        login_btn.click()

        sleep(15)



    def tasker(self):
        task_btn = self.driver.find_element("xpath",'//*[@id="id_tasks_link"]')
        task_btn.click()
        sleep(2)
        extend_btn = self.driver.find_element("xpath",'//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr/td[6]/button[4]')
        extend_btn.click()



bot = TaskerBot()
bot.login()
bot.tasker()
