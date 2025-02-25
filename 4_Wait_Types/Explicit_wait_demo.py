from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitDemo():

    def runtest(self):
        # baseUrl = "https://www.letskodeit.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseUrl)
        driver.execute_script("window.location = 'https://www.letskodeit.com/home';")

        wait = WebDriverWait(driver, timeout=10, poll_frequency=4, ignored_exceptions= [NoSuchFrameException,
                                                                                        ElementNotSelectableException,
                                                                                        ElementNotVisibleException])

        element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/login"]')))  #login element
        element.click()
        time.sleep(4)

        emailField = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
        emailField.send_keys("test")
        time.sleep(2)

        driver.quit()

test = ExplicitWaitDemo()
test.runtest()
