from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class BrowseInteractions():

    def runtest(self):
        baseurl = "https://www.letskodeit.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        loginlink = driver.find_element(By.XPATH,'//div[@id="navbar-inverse-collapse"]/div')
        loginlink.click()

        email = driver.find_element(By.XPATH, '//*[@id="email"]')
        email.send_keys('1st testing')

        password = driver.find_element(By.ID, 'login-password')
        password.send_keys('test')

        time.sleep(5)
        email.clear()
        time.sleep(5)
        email.send_keys('2nd testing')
        time.sleep(2)

test = BrowseInteractions()
test.runtest()
