import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyIDName():

    def runtest(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementbyID = driver.find_element(By.ID, "bmwradio")
        if elementbyID is not None:
            print("Element Found By ID!" + elementbyID.text)

        elementbyName = driver.find_element(By.NAME, "show-hide")
        if elementbyName is not None:
            print("Element found by Name!")

        elementbyXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elementbyXpath is not None:
            print("Element found by XPath!")

        elementbyCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementbyCSS is not None:
            print("Element found by CSS Selector!" + elementbyCSS.text)

        elementbyLink = driver.find_element(By.LINK_TEXT, "HOME")
        if elementbyLink is not None:
            print('element found by link-text!')

        elementbypartiallink = driver.find_element(By.PARTIAL_LINK_TEXT, 'COURSES')
        if elementbypartiallink is not None:
            print('element found by Partial link-text!')

        elementbyclassname = driver.find_element(By.CLASS_NAME, "inputs")
        if elementbyLink is not None:
            print('element found by class name!')
            elementbyclassname.send_keys('WRITE TEXT')

        elementbytagname = driver.find_element(By.TAG_NAME, 'a')
        if elementbypartiallink is not None:
            print('element found by Partial link-text!' + elementbytagname.text)

        time.sleep(10)

test = FindbyIDName()
test.runtest()
