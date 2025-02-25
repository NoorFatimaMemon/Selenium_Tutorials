from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetValueofElement():

    def runtest(self):
        baseURL = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        findElement = driver.find_element(By.ID, 'openwindow')
        GetValue = findElement.get_attribute('class')
        print('The Attribute Value is: ' + GetValue)
        #time.sleep(1)

        findElement2 = driver.find_element(By.ID, 'multiple-select-example')
        GetValue2 = findElement2.get_attribute('name')
        print('The Attribute Value is: ' + GetValue2)
        #time.sleep(1)
        driver.quit()


test = GetValueofElement()
test.runtest()
