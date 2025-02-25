from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingwithElementsList():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        radiobtnlist = driver.find_elements(By.XPATH, '//input[contains(@type,"radio") and contains(@name,"cars")]')
        size = len(radiobtnlist)
        print('size of the list of the radio button: ' + str(size))

        for radiobtn in radiobtnlist:
            isSelected = radiobtn.is_selected()

            if not isSelected:
                radiobtn.click()
                time.sleep(5)

test= WorkingwithElementsList()
test.runtest()
