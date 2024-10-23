from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from util.constants import CHROME_DRIVER_PATH, LINK_CASA_DOS_DADOS, PROXY#GECKO_DRIVER_PATH
from util.janelas import SiteCarregado, FiltrosSelecionados

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
        SiteCarregado()
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div[1]/nav/div[2]/div/a[2]").click()

    def _configura_driver(self):
        options = ChromeOptions()
        # BRAVE_PATH = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

        # options.page_load_strategy = "eager"
        driver = webdriver.Chrome(
            service=Service(
                CHROME_DRIVER_PATH
                ),
            options=options
            )
        driver.implicitly_wait(5)
        return driver
