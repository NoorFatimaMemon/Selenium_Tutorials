from selenium import webdriver
import os

class RunChromeTests():

    def test(self):
        driver_location = 'C:\\Users\\Noor\\PycharmProjects\\SeleniumWDTutorial\\drivers\\chrome_driver_windows.exe'
        os.environ["webdriver.chrome.driver"] = driver_location
        driver = webdriver.Chrome(driver_location)
        driver.get("https://www.letskodeit.com")

runtests = RunChromeTests()
runtests.test()
