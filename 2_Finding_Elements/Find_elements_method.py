import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class listofElements():

    def runtest(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementlistbyclassname = driver.find_elements(By.CLASS_NAME, "dropbtn")
        length1 = len(elementlistbyclassname)
        if elementlistbyclassname is not None:
            print("Size of the Elements Found By Class Name: " + str(length1))

        elementlistbytagName = driver.find_elements(By.TAG_NAME, "a")
        length2 = len(elementlistbytagName)
        if elementlistbytagName is not None:
            print("Size of the Elements found by Tag Name: " + str(length2))

        elementlistbyxpath = driver.find_elements(By.XPATH, '//*[@id="checkbox-example-div"]/fieldset/label[1]')
        length3 = len(elementlistbyxpath)
        if elementlistbyxpath is not None:
            print("Size of the Elements Found By Xpath: " + str(length3))

        time.sleep(2)

test = listofElements()
test.runtest()
