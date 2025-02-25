from selenium import webdriver
# from selenium.webdriver.common.by import By


class JavaScriptExecution():

    def runtest(self):
        # baseURL = 'https://www.letskodeit.com/home'
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseURL)
        driver.execute_script("window.location = 'https://www.letskodeit.com/login';")
        driver.implicitly_wait(5)

        Height = driver.execute_script("return window.innerHeight;")
        Width = driver.execute_script("return window.innerWidth;")
        print("Height of the widow is: " + str(Height))
        print("Width of the widow is: " + str(Width))
        driver.quit()

    def runtest2(self):
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.execute_script("window.location = 'https://www.letskodeit.com/login';")
        driver.implicitly_wait(5)

        Height = driver.execute_script("return window.innerHeight;")
        Width = driver.execute_script("return window.innerWidth;")
        print("Height of the widow is: " + str(Height))
        print("Width of the widow is: " + str(Width))
        driver.quit()


test = JavaScriptExecution()
test.runtest()
test.runtest2()
