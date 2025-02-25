import time
from selenium import webdriver
from HandyWrappers import HandyWrappers

class UsingHandyWrappers:

    def runtest(self):
        sourcelink = 'https://www.letskodeit.com/practice'
        driver = webdriver.Chrome()
        hw = HandyWrappers(driver)
        driver.get(sourcelink)
        driver.implicitly_wait(2)

        # Return Lists of Elements
        hw.GetElements('//select[@id="multiple-select-example"]//option', LocatorType='xpath')

        # Element Click
        hw.ClickElement('//input[@id="bmwradio"]', LocatorType='xpath')
        time.sleep(2)

        # Get Element Text
        hw.GetElementText('//*[@id="product"]/tbody/tr[3]/td[2]', LocatorType='xpath')

        # Get Elements list of Text
        hw.GetElementlistofText('//select[@id="multiple-select-example"]//option', 'xpath')

        # Get Element Attribute
        hw.GetElementAttribute('mousehover', LocatorType='id', attribute='class')

        # Get Elements list of attribute value
        hw.GetElementlistofattribute('//select[@id="multiple-select-example"]//option', 'xpath', 'value')

        # Element Present or not
        hw.isElementPresent('//input[@id="bmwradio"]', 'xpath')


test = UsingHandyWrappers()
test.runtest()
