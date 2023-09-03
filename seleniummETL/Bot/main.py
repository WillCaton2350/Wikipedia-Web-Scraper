from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as WDW
from States.data import searchBtn, bio1,bio2,bio3,title_Xpath
from urllib.error import HTTPError as PageNotFoundError
from States.data import geckoDriverPath, search_Xpath
from selenium.webdriver.common.by import By 
from selenium import webdriver as web 
import pandas
import os

url= "https://www.wikipedia.org/"
class webDriver:
    def __init__(self):
        self.driver = None 
    def startDriver(self):
        firefox_options = web.FirefoxOptions()
        self.driver = web.Firefox(
            options=firefox_options
        )
        os.environ[
            "webdriver.firefox.driver"
            ] =  geckoDriverPath
        self.driver.maximize_window()
    def Browser(self):
        self.driver.get(url)
        try:
            WDW(
                self.driver, 
                timeout=10).until(
                    EC.url_matches(
                        url))
        except PageNotFoundError as err:
            if err.code == 404:
                print(
        "Error: Page not found")
    def searchBar(self):
        self.driver.find_element(
            By.XPATH,search_Xpath).send_keys("Megalodon")
        self.driver.find_element(
            By.XPATH,searchBtn).click()
    def actions1(self):
        titleObj = self.driver.find_elements(By.XPATH,title_Xpath )
        getTitle = [title.text for title in titleObj]
        dataFrame = pandas.DataFrame({'Title':getTitle})
        bio1Obj = self.driver.find_elements(By.XPATH,bio1)
        getB_bio1 = [b1.text for b1 in bio1Obj]
        dataFrame2 = pandas.DataFrame({'Bio - 1':getB_bio1})
        print(dataFrame,dataFrame2)
        return(dataFrame,dataFrame2)
    def actions2(self):
        bio2Obj = self.driver.find_elements(By.XPATH, bio2)
        get_bio2 = [b2.text for b2 in bio2Obj]
        dataFrame3 = pandas.DataFrame({'Bio - 2':get_bio2})
        print(dataFrame3)
        bio3Obj = self.driver.find_elements(By.XPATH,bio3)
        get_bio3 = [b3.text for b3 in bio3Obj]
        dataframe4 = pandas.DataFrame({'Bio - 3':get_bio3})
        print(dataframe4)
        return(dataFrame3,dataframe4)
    def closeBrowser(self):
        self.driver.quit()

