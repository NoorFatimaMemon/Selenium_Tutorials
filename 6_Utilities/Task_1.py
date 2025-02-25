import time
import datetime
from selenium import webdriver
from HandyWrappers import HandyWrappers

class Task1:

    def task_1(self):
        sourcelink = 'https://www.w3schools.com/'
        driver = webdriver.Chrome()
        hw = HandyWrappers(driver)
        driver.get(sourcelink)
        driver.implicitly_wait(2)

        # Click on Tutorials
        hw.ClickElement('//a[@id="navbtn_tutorials"]//i[1]', LocatorType='xpath')
        time.sleep(1)

        # Click on Learn Python.
        hw.ClickElement('//a[@href="/python/default.asp"]', LocatorType='xpath')
        time.sleep(1)

        # Click on Python Intro
        hw.ClickElement('//a[contains(@target,"_top") and contains(@href,"python_intro.asp")]', LocatorType='xpath')
        time.sleep(1)

        # Data Scraping
        Element_list_of_Text = hw.GetElementlistofText('//*[@id="main"]/ul[5]//li', 'xpath')
        Element_into_string = " ".join(Element_list_of_Text)

        # Storing data in txt file with modified Date and Time.
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d, %H-%M-%S")
        fileLocation = str(current_datetime) + '.txt'
        with open(fileLocation, "w") as file:
            file.write(Element_into_string)


test = Task1()
test.task_1()
