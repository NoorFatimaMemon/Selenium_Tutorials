from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        # Find the state of the text box
        ElementTextBox = driver.find_element(By.ID, 'displayed-text')
        ElementTextBoxState = ElementTextBox.is_displayed()  # True if visible, False if hidden, Exception if not present in DOM
        print('Text is visible? ' + str(ElementTextBoxState))
        time.sleep(3)

        # Click the Hide button
        driver.find_element(By.ID, 'hide-textbox').click()
        time.sleep(3)

        ElementTextBoxState = ElementTextBox.is_displayed()
        print('Text is visible? ' + str(ElementTextBoxState))
        time.sleep(3)

        # Click the Show button
        driver.find_element(By.ID, 'show-textbox').click()
        time.sleep(3)

        ElementTextBoxState = ElementTextBox.is_displayed()
        print('Text is visible? ' + str(ElementTextBoxState))
        time.sleep(3)

    def testExpedia(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH, '//div[@id="wizardMainRegionV2"]/div/div/div/div/ul/li[2]/a/span').click()
        time.sleep(5)

        drpdwnElement = driver.find_element(By.ID, 'child-age-input-0-0')
        print('Text is visible? ' + str(drpdwnElement.is_displayed()))
        time.sleep(4)

test = HiddenElements()
test.runtest()
test.testExpedia()
