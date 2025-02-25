from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DropdownSelect:

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        elementtobeselected = driver.find_element(By.ID, 'carselect')
        sel = Select(elementtobeselected)

        sel.select_by_value('benz')
        print('Select Benz by Value ')
        time.sleep(3)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text('BMW')
        print('Select BMW by visible text ')
        time.sleep(3)

        sel.select_by_index(2)
        print('Select Honda by index ')
        time.sleep(3)


test = DropdownSelect()
test.runtest()
