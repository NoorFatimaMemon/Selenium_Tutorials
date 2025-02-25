from selenium import webdriver
from HandyWrappers import HandyWrappers
from selenium.webdriver.common.by import By
import time

class ElementPresentCheck():

    def runtest(self):
        sourcelink = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        hw = HandyWrappers(driver)
        driver.get(sourcelink)
        driver.implicitly_wait(10)

        elementresult1 = hw.isElementPresent('name', By.ID)
        print(str(elementresult1))

        elementresult2 = hw.isElementPresent('//[input=[@id="name"]', By.ID)
        print(str(elementresult2))

        element2 = hw.ElementPresenceCheck("name", By.ID)
        print(str(element2))

test = ElementPresentCheck()
test.runtest()
