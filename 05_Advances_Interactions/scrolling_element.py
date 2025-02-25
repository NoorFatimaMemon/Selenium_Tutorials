import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class JavaScriptExecution():

    def runtest(self):
        # baseURL = 'https://www.letskodeit.com/home'
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver.get(baseURL)
        driver.execute_script("window.location = 'https://www.letskodeit.com/practice';")
        driver.implicitly_wait(5)

        # Scroll down fully
        driver.execute_script('window.scrollBy(0, 900)')
        time.sleep(3)

        # Scroll Up fully
        driver.execute_script('window.scrollBy(0, -700)')
        time.sleep(3)

        # Scroll up to the element we want
        element = driver.find_element(By.ID, 'mousehover')
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        time.sleep(5)
        driver.execute_script('window.scrollBy(0, -700)')
        time.sleep(5)

        # Scroll up to the element we want (Native Way)
        location = element.location_once_scrolled_into_view
        print("location: " + str(location))
        time.sleep(5)

test = JavaScriptExecution()
test.runtest()
