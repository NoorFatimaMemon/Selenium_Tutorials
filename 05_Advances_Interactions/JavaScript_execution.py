from selenium import webdriver
# from selenium.webdriver.common.by import By
import time


class JavaScriptExecution():

    def runtest(self):
        # baseURL = 'https://www.letskodeit.com/home'
        driver = webdriver.Chrome()
        # driver.maximize_window()
        # driver.get(baseURL)
        driver.execute_script("window.location = 'https://www.letskodeit.com/login';")
        driver.implicitly_wait(5)
        time.sleep(3)

        # email_login = driver.find_element(By.ID, "name")
        email_login = driver.execute_script("return document.getElementById('email');")
        email_login.send_keys('test')
        time.sleep(4)

        # elements by class name
        Elements = driver.execute_script("return document.getElementsByClassName('col-md-12 col-sm-12 padding-top-50 padding-bottom-50');")
        print(len(Elements))
        time.sleep(4)


test = JavaScriptExecution()
test.runtest()
