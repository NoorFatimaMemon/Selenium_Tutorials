from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        FindElement = driver.find_element(By.ID, 'mousehover')
        FindElementText = FindElement.text
        print("Element Text is: " + FindElementText)
        # time.sleep(2)

        FindElementText2 = FindElement.get_attribute("innerText")
        print("Element Text is: " + FindElementText2)
        # time.sleep(2)

        FindElement2 = driver.find_element(By.XPATH, '//*[@id="product"]/tbody/tr[2]/td[1]')
        FindElementText2 = FindElement2.text
        print("Second Element Text is: " + FindElementText2)
        # time.sleep(2)
        driver.quit()

test = GetText()
test.runtest()
