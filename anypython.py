from selenium import webdriver
from time import sleep
from secrets import username, password


class TaskerBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

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
