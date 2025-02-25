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

            # Save headings as keys and subheadings as values in a dictionary (use for loops and remove indexes method)
            unorderdict = {}
            for key in reversed_headings:
                values = self.hw.GetElementlistofText(f'//h2[.="{key}"]//following-sibling::a', 'xpath')
                unorderdict[key] = values

            print(unorderdict)
            heading_input = input("Enter a heading (or key): ")

            list_of_headings = list(unorderdict.keys())  # list of keys
            heading_index = list_of_headings.index(heading_input)  # user input heading index

            if heading_index > 0:
                previous_heading = list_of_headings[heading_index - 1]  # accessing to previous key of the dictionary
                subheadings_of_previous_heading = unorderdict[previous_heading]  # accessing values of previous key of the dictionary
                updated_list_of_subheadings = []

                # update the list of the subheadings we want
                for value in unorderdict[heading_input]:
                    if value not in subheadings_of_previous_heading:
                        updated_list_of_subheadings.append(value)
                    else:
                        "Nothing to show!"
                print(updated_list_of_subheadings)

            else:
                updated_list_of_subheadings = unorderdict[heading_input]
                print(updated_list_of_subheadings)

            return updated_list_of_subheadings

test = Task3()
test.task_3()
