from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScreeShots():

    def runtest(self):
        baseURL = 'https://www.letskodeit.com/home'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(By.XPATH, '//input[@placeholder="Email Address"]').send_keys('noormemon457@gmail.com')
        driver.find_element(By.ID, 'login-password').send_keys('abcd')
        time.sleep(3)
        driver.find_element(By.ID, 'login').click()
        time.sleep(3)
        self.takescreeshots(driver)

    def takescreeshots(self, driver):  # SS generic methods (Takes screenshot of the current open web page)
        filename = str(round(time.time() * 1000)) + '.png'
        directoryname = 'C:\\Users\\Noor\\PycharmProjects\\SeleniumWDTutorial\\AdvancesInteractions_5\\'
        completefilename = directoryname + filename

        try:
            driver.save_screenshot(completefilename)
            print("SS saved in the directory!")

        except NotADirectoryError:
            print('Not a directory error')


test = ScreeShots()
test.runtest()
