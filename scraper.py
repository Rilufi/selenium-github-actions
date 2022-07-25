from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import os

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

driver1 = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver2 = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver3 = webdriver.Chrome(service=chrome_service, options=chrome_options)

video_link = "https://www.youtube.com/watch?v=_YRCdt890PE&t"

driver1.get(video_link)
driver2.get(video_link)
driver3.get(video_link)
#i have used siddharth 1,2,3  so it will open 3 tabs 
#if you want to add more tabs you can also do it 

while True:
    sleep(18)#sleep 18 meanes after 18 seconds page will refresh
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
