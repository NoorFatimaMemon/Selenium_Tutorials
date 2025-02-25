from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)
        driver.execute_script('window.scrollBy(0, 700);')
        time.sleep(3)

        driver.find_element(By.XPATH, '//button[@id="mousehover"]').click()
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, 'Top').click()
        time.sleep(2)

    def runtest2(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.execute_script('window.scrollBy(0, 700);')
        time.sleep(3)

        element = driver.find_element(By.XPATH, '//button[@id="mousehover"]')
        item_locator = "Top"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print('Mouse hovered on element')
            item_to_locate = driver.find_element(By.LINK_TEXT, item_locator)
            actions.move_to_element(item_to_locate).click().perform()
            time.sleep(2)
            print('item clicked!')

        except:
            print('Mouse hovered failed')

test = MouseHovering()
test.runtest2()
