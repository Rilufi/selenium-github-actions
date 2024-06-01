from secrets import usuario, senha
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = Options()
# Update the path to your downloaded ChromeDriver (replace with actual path)
chrome_driver_path = "/tmp/chromedriver"

chrome_options = Options()
# Comment out these options if they cause problems
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=ChromeDriverManager().install(),options=chrome_options)

#driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

def login():
        driver.get('https://cp.ravenro.com.br/')
        sleep(2)
    #   fb_btn = self.driver.find_element(By.CLASS_NAME,'login_link')
     #  fb_btn.click()
        email_in = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/input[1]')
        email_in.send_keys(usuario)
        pw_in = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/input[2]')
        pw_in.send_keys(senha)
        login_btn = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[2]/div/button[1]')
        login_btn.click()
        sleep(5)

def tasker():
        driver.get('https://cp.ravenro.com.br/votar')
        sleep(2)
        task_btn.click()
        sleep(2)
        extend_btn = self.driver.find_element("xpath",'/html/body/div[1]/div[2]/div/div/div[5]/div[2]/div/div[2]/div[2]/button')
        extend_btn.click()
        sleep(2)
try:
    login()
    tasker()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Always close the browser window

bot = login()  # Assuming login returns an object (modify if needed)
# bot.tasker()  # Uncomment if login doesn't return an object
