from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        # Find parent handle in Main Window
        First_Handle = driver.current_window_handle
        print('Parent Handle = ' + First_Handle)

        # Find open window button and click it
        driver.find_element(By.ID, 'openwindow').click()
        time.sleep(2)

        # Find all handles, there should two handles after clicking open window button
        All_Handles = driver.window_handles

        for handle in All_Handles:
            print("Handle = " + handle)
            if handle not in First_Handle:
                driver.switch_to.window(handle)
                print('Switched Window is ' + handle)
                Search_Course_Box = driver.find_element(By.XPATH, '//input[@id="search"]')
                Search_Course_Box.send_keys('selenium')
                time.sleep(3)
                driver.close()
                break

        # Switch to window and search course
        driver.switch_to.window(First_Handle)
        element = driver.find_element(By.XPATH, '//input[@name="enter-name"]')
        element.send_keys('test')
        time.sleep(3)
        driver.quit()


test = SwitchToWindow()
test.runtest()
