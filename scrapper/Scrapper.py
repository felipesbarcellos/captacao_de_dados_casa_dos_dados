from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from util.constants import CHROME_DRIVER_PATH, LINK_CASA_DOS_DADOS #PROXY, GECKO_DRIVER_PATH
from util.janelas import SiteCarregado, FiltrosSelecionados
from selenium_stealth import stealth
import random

class ScrapperCasaDosDados():
    def __init__(self):
        self.driver = self._configura_driver()
        self.pagina = LINK_CASA_DOS_DADOS
        self._acessa_pagina()
        ...

    def run():
        ...

    def _acessa_pagina(self):
        self.driver.get(self.pagina)
        self.driver.save_screenshot('teste.png')
        SiteCarregado()
        self.driver.close()
        # self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/nav/div[2]/div/a[2]").click()

    def _configura_driver(self):
        options = ChromeOptions()
        # options.add_argument("start-maximized")
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        # options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--headless=old")

        # BRAVE_PATH = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

        # options.page_load_strategy = "eager"
        driver = webdriver.Chrome(
            service=Service(
                CHROME_DRIVER_PATH
                ),
            options=options
            )
        driver.implicitly_wait(5)
        stealth(
            driver=driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win62",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        )
        return driver
