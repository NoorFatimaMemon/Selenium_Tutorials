from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class elementstate():

    def isEnabled(self):
        baseurl = 'https://www.google.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        x1 = driver.find_element(By.CLASS_NAME, 'YacQv')
        x1state = x1.is_enabled()
        print('x1 is enabled: ' + str(x1state))

        x2 = driver.find_element(By.CLASS_NAME, 'gLFyf')
        x1state = x2.is_enabled()
        print('x2 is enabled: ' + str(x1state))

        x2.send_keys('new test')
        time.sleep(4)

y=elementstate()
y.isEnabled()
