from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.support.ui import Select 
import time

class finder():
    city = None
    def scraping(self): 
        options = Options()
        options.add_experimental_option("detach", True)
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                options=options)

        driver.get("https://www.olx.pl")
        driver.maximize_window()

        menu = driver.find_element(By.ID, "headerSearch")
        location = driver.find_element(By.ID, "cityField")
        search = driver.find_element(By.ID, "submit-searchmain")
        links = driver.find_elements(By.ID, "onetrust-accept-btn-handler")
        
        for link in links:
            link.click()
        actions = ActionChains(driver)
        actions.click(menu)
        actions.send_keys("koty do adopcji")
        actions.perform()
        actions.click(location)
        actions.send_keys(self.city)
        actions.perform()
        time.sleep(2)
        actions.click(search)
        actions.perform()
        time.sleep(2)
        sorting = driver.find_element(By.CSS_SELECTOR, "[data-testid=\"sorting-wrapper\"]")
        actions.click(sorting)
        actions.perform()
        sorting_options = driver.find_elements(By.CSS_SELECTOR, "[data-testid=\"sorting-option\"]")
        for sorting_option in sorting_options:
            if sorting_option.text == 'Najnowsze':
                actions.click(sorting_option)
                actions.perform()
                break

    def __init__(self, city):
        self.city = city
