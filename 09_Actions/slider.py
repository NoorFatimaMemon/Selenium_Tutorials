from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Slider():

    def runtest2(self):
        baseurl = 'https://jqueryui.com/slider/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.switch_to.frame(0)

        element = driver.find_element(By.XPATH, '//div[@id="slider"]//span')
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(element, 500, 0).perform()
            print('Sliding Element successful')
            time.sleep(2)

        except:
            print('Sliding Element failed')

test = Slider()
test.runtest2()
