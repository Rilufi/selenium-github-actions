from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep, time
from datetime import datetime
from selenium.webdriver.common.by import By


timeout_start = time()

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


class Bot:
    def __init__(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
    
    def read_arq(self):
        '''
        Le o arquivo com os links e os coloca em uma lista
        return: list
        '''
        try:
            with open('links.txt', 'r') as arquivo:
                links = [linha.strip() for linha in arquivo.readlines()]
            return links
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha na leitura do arquivo!
                {error}\n{"-"*50}''')

    def open_url(self, url):
        '''
        Get na url passada.
        '''
        try:
            self.browser.get(url)
        except Exception as error:
            print(
                f'''{"-"*50}\nFalha ao entrar na URL passada!
                {error}\n{"-"*50}''')

    def get_video_name(self):
        '''
        Pega o nome do video que esta sendo assistido
        '''
        try:
            name = self.browser.find_element(
                By.CSS_SELECTOR, '#container > h1 > yt-formatted-string')
            print(name.text)
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting current video name!
                {error}\n{"-"*50}''')

    def get_video_duration(self):
        '''
        Pega a duracao total do video que esta sendo assistido
        '''
        try:
            duration = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-duration')
            return duration.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting video duration!
                {error}\n{"-"*50}''')

    def speed_up(self):
        '''
        Coloca a velocidade do video que esta sendo assitido em 2x
        '''
        try:
            teste = self.browser.find_element(
                By.CSS_SELECTOR, '.ytp-settings-button')
            teste.click()
            teste.send_keys('m')
            for i in range(4):
                teste.send_keys(Keys.SHIFT + '.')
        except Exception as error:
            print(f'{"-"*50}\nFail to speed up! \n\n{error}\n{"-"*50}')

    def get_time_watched(self):
        '''
        Pega o tempo de video que foi visto
        '''
        try:
            time_watched = self.browser.find_element(
                By.CLASS_NAME, 'ytp-time-current')
            return time_watched.text
        except Exception as error:
            print(
                f'''{"-"*50}\nFail getting current video time!
                {error}\n{"-"*50}''')
    
    def play_video(self):
        '''
        Clica no botao play
        '''
        try:
            play_btn = self.browser.find_element(
                By.CSS_SELECTOR, '.ytp-play-button')
            play_btn.click()
        except Exception as error:
            print(
                f'{"-"*50}\nFail to play! \n\n{error}\n{"-"*50}')

    def close_browser(self):
        '''
        Fecha o browser
        '''
        try:
            self.browser.close()
        except Exception as error:
            print(f'{"-"*50}\nFail to close the browser!\n\n{error}\n{"-"*50}')


#reader = readChannels.channelReader()
#links = reader.get_videos()
#reader.writeTxt(links)
timeout = 21500

load_links = Bot()  #aqui ta abrindo uma tela sozinho
links = load_links.read_arq()
while time() < timeout_start + timeout:
    for view in range(50):
        for video in links:
            bot = Bot()
            bot.open_url(video)
            print('-'*100 + '->')
            print(video)
            sleep(3)
            bot.get_video_name()
            total_dur = bot.get_video_duration()
            bot.speed_up()
            sleep(2)
            test = bot.get_time_watched()
            if test == '0:00':
                bot.play_video()
                print('Forced play!')
            print(f'Watching! {datetime.now():%d-%m-%y %H:%M:%S}')
            time_before = datetime.now()
            watched = 0
            while total_dur != watched:
                if watched == 0:
                    sleep(1)
                watched = bot.get_time_watched()
                time_after = datetime.now() - time_before
                if time_after.seconds >= 480:
                    print('Bug or ad too long, starting next video!')
                    break

            print(f'View {view+1} completa!')
            print('-'*100 + '->')
            print()
            sleep(1)
            bot.close_browser()
