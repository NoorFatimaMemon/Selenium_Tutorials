from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ImplicitWaitDemo():
    def test(self):
        baseUrl = "https://www.letskodeit.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(4)

        loginLink = driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a')
        loginLink.click()


        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test")

ff = ImplicitWaitDemo()
ff.test()
