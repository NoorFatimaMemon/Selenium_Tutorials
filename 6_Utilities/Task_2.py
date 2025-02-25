import time
from selenium import webdriver
from HandyWrappers import HandyWrappers

class Task2:

    def task2a(self):
        sourcelink = 'https://www.w3schools.com/'
        driver = webdriver.Chrome()
        hw = HandyWrappers(driver)
        driver.get(sourcelink)
        driver.implicitly_wait(1)

        # Click on Tutorials
        hw.ClickElement('//a[@id="navbtn_tutorials"]//i[1]', LocatorType='xpath')
        time.sleep(1)

        # Click on Learn Python.
        hw.ClickElement('//a[@href="/python/default.asp"]', LocatorType='xpath')
        time.sleep(1)

        # Click on Python Intro
        hw.ClickElement('//a[contains(@target,"_top") and contains(@href,"python_intro.asp")]', LocatorType='xpath')
        time.sleep(1)

        # Get headings & subheadings
        Element_list_of_Text = hw.GetElementlistofText('//div[@id="leftmenuinnerinner"]', 'xpath')
        for elements_text in Element_list_of_Text:
            if elements_text is not None or False:
                print(elements_text)
            else:
                print("Element text not exist!")

    def task2b(self):
        sourcelink = 'https://www.w3schools.com/'
        driver = webdriver.Chrome()
        hw = HandyWrappers(driver)
        driver.get(sourcelink)
        driver.implicitly_wait(1)

        # Click on Tutorials
        hw.ClickElement('//a[@id="navbtn_tutorials"]//i[1]', LocatorType='xpath')
        time.sleep(1)

        # Click on Learn Python.
        hw.ClickElement('//a[@href="/python/default.asp"]', 'xpath')
        time.sleep(1)

        # Click on Python Intro
        hw.ClickElement('//a[contains(@target,"_top") and contains(@href,"python_intro.asp")]', 'xpath')
        time.sleep(1)

        # Get all the subheadings of input heading
        heading = input("Enter a heading:  ")
        elements = hw.GetElements(f'//h2[.="{heading}"]//following-sibling::*', 'xpath')
        for element in elements:
            tag = element.tag_name
            if tag == 'br':
                break
            else:
                print(element.text)


test = Task2()
test.task2b()
