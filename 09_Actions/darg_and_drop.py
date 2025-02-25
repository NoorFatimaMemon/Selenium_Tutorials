from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def runtest2(self):
        baseurl = 'https://jqueryui.com/droppable/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.switch_to.frame(0)

        from_element = driver.find_element(By.ID, 'draggable')
        to_element = driver.find_element(By.ID, 'droppable')

        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(from_element, to_element).perform()
            actions.click_and_hold(from_element).move_to_element(to_element).release().perform()
            print('Element dragged and then dropped = test successful')
            time.sleep(2)

        except:
            print('test failed')

test = DragAndDrop()
test.runtest2()
