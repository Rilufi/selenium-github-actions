from selenium import webdriver
from time import sleep
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.parperfeito.com.br/')

        sleep(2)

        cookie = self.driver.find_element("xpath",'//*[@id="onetrust-accept-btn-handler"]')
        cookie.click()

        sleep(2)

        fb_btn = self.driver.find_element("xpath",'//*[@id="__next"]/div/div/div/button/span')
        fb_btn.click()

        email_in = self.driver.find_element("xpath",'//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element("xpath",'//*[@id="password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element("xpath",'//*[@id="mainContent"]/form/div/div[1]/div[5]/button/span')
        login_btn.click()

        sleep(15)



    def like(self):
        like_btn = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/span/button/span/div[2]')
        like_btn.click()
    def like2(self):
        like_btn2 = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/span/button')
        like_btn2.click()

    def dislike(self):
        dislike_btn = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div[2]/button/span/span[2]')
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
        popup_3 = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[3]/div/div[2]/div/button')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element("xpath",'//*[@id="mainContent"]/div[2]/section/div[1]/div/div[4]/div/div[2]/div/button')
        match_popup.click()


bot = TinderBot()
bot.login()

try:
    bot.auto_swipe()
except:
    ask = input("Deseja continuar? ")
    if ask != 'n':
        bot.auto_swipe()
    else:
        pass
