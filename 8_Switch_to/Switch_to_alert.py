from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToAlert():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        driver.find_element(By.ID, 'name').send_keys('Noor')
        driver.find_element(By.ID, 'alertbtn').click()
        time.sleep(3)

        alert1 = driver.switch_to.alert           # switch to alert tab
        alert1.accept()
        time.sleep(3)

        driver.find_element(By.ID, 'name').send_keys('Memon')
        driver.find_element(By.ID, 'confirmbtn').click()
        time.sleep(3)

        alert2 = driver.switch_to.alert
        alert2.dismiss()
        time.sleep(3)


test = SwitchToAlert()
test.runtest()
