from selenium import webdriver
from Wait_Types_4.Explicit_wait_type import ExplicitWaitType
import time


class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "https://www.letskodeit.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        wait = ExplicitWaitType(driver)
        element2 = wait.WaitForElement(Locator='//*[@id="navbar-inverse-collapse"]/div/div/a', LocatorType='xpath')
        element2.click()

        time.sleep(4)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()
