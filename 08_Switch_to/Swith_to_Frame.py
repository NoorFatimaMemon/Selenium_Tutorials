from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.execute_script('window.scrollBy(0, 1000);')

        # Switch to frame using Id
        # driver.switch_to.frame('courses-iframe')

        # Switch to frame using name
        # driver.switch_to.frame('iframe-name')

        # Switch to frame using numbers
        driver.switch_to.frame(0)
        time.sleep(3)

        element = driver.find_element(By.XPATH, '//input[@placeholder="Search Course"]')
        element.send_keys('Python')
        time.sleep(3)

        # Switch back to the parent frame
        driver.switch_to.default_content()
        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(3)
        driver.find_element(By.ID, 'autosuggest').send_keys("Successful Test!")
        time.sleep(4)

test = SwitchToFrame()
test.runtest()
