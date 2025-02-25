import time
from selenium import webdriver
from HandyWrappers import HandyWrappers

class Task3:
    sourcelink = 'https://www.w3schools.com/'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)

    def task_3(self):
        # Click on Tutorials
        self.hw.ClickElement('//a[@id="navbtn_tutorials"]//i[1]', LocatorType='xpath')
        time.sleep(1)

        # Click on Learn Python.
        self.hw.ClickElement('//a[@href="/python/default.asp"]', 'xpath')
        time.sleep(1)

        # Click on Python Intro
        self.hw.ClickElement('//a[contains(@target,"_top") and contains(@href,"python_intro.asp")]', 'xpath')
        time.sleep(1)

        # Get all the subheadings of input heading
        list_of_heading = self.hw.GetElementlistofText('//*[@id="leftmenuinnerinner"]//h2', 'xpath')
        reversed_headings = reversed(list_of_heading)

        # Save headings as keys and subheadings as values in a dictionary
        unorderdict = {}
        list1 = []
        heading_input = input("Enter a heading (or key): ")
        for key in reversed_headings:
            values = self.hw.GetElementlistofText(f'//h2[.="{key}"]//following-sibling::a', 'xpath')
            unorderdict[key] = values

        previous_key = None

        for current_key in unorderdict:
            if current_key == heading_input and previous_key is not None:
                previous_value = unorderdict[previous_key]
                current_value = unorderdict[current_key]
                for i in current_value:
                    if i not in previous_value:
                        list1.append(i)
                    else:
                        pass
            previous_key = current_key

        print(list1)
        return list1


test = Task3()
test.task_3()
