from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonandCheckBoxes():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        bmwRadiobtn = driver.find_element(By.ID, 'bmwradio')
        bmwRadiobtn.click()
        time.sleep(2)

        benzRadiobtn = driver.find_element(By.ID, 'benzradio')
        benzRadiobtn.click()
        time.sleep(2)

        bmwcheckbtn = driver.find_element(By.ID, 'bmwcheck')
        bmwcheckbtn.click()
        time.sleep(2)

        benzcheckbtn = driver.find_element(By.ID, 'benzcheck')
        benzcheckbtn.click()
        time.sleep(2)

        hondacheckbtn = driver.find_element(By.ID, 'hondacheck')
        hondacheckbtn.click()
        time.sleep(2)

        print('bmw radio button selected? ' + str(bmwRadiobtn.is_selected()))
        print('benz radio button selected? ' + str(benzRadiobtn.is_selected()))
        print('bmw check button selected? ' + str(bmwcheckbtn.is_selected()))
        print('benz check button selected? ' + str(benzcheckbtn.is_selected()))
        print('honda check button selected? ' + str(hondacheckbtn.is_selected()))

test= RadioButtonandCheckBoxes()
test.runtest()
