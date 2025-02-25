from selenium import webdriver
from HandyWrappers import HandyWrappers
import time

class Task4:
    sourcelink = 'https://www.w3schools.com/'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)
    driver.implicitly_wait(2)

    def task_4(self):
        # Click on Tutorials
        self.hw.ClickElement('//a[@id="navbtn_tutorials"]//i[1]', LocatorType='xpath')
        time.sleep(1)

        # Click on Learn Python.
        self.hw.ClickElement('//a[@href="/python/default.asp"]', 'xpath')
        time.sleep(1)

        # Click on Python Intro
        subheading_input = input("Enter a subheading: ")

        self.hw.ClickElement(f'//a[text()="{subheading_input}"]', 'xpath')
        time.sleep(3)

        # Data Scraping
        headings = self.hw.GetElementlistofText('//h5', "xpath")
        Final_list = []
        for heading in headings:
            subheadings = self.hw.GetElementlistofText(f'//h5[.="{heading}"]//parent::*//following-sibling::a',
                                                       'xpath')
            for subheading in subheadings:
                links = self.hw.GetElementlistofattribute(f"//h5//parent::*//parent::div//a[.='{subheading}']", "xpath", "href" )
                for link in links:
                    Final_list.append([heading, subheading, link])

        print(Final_list)
        return Final_list


"""test = Task4()
test.task_4()"""
