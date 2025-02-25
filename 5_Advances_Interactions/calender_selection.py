import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class CalenderSelectionPractice():

    def runtest1(self):
        baseUrl = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        # Click flights tab
        FlightTab = driver.find_element(By.LINK_TEXT, 'Flights')
        FlightTab.click()

        # Find & click departing field
        LeavingField = driver.find_element(By.XPATH, '//button[@data-name="d1"]')
        LeavingField.click()
        time.sleep(4)

        # Find the date to be selected
        DatetobeSelected = driver.find_element(By.XPATH,
                                               '//td[@class="uitk-date-picker-day-number"][position()=7]//button[@data-day="15"]')
        DatetobeSelected.click()
        time.sleep(4)

    def runtest2(self):
        baseUrl = 'https://www.southwest.com/'
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        # Click flights tab
        driver.find_element(By.XPATH, '//button[@id="TabbedArea_4-tab-0"]').click()
        time.sleep(2)

        # Find & click departing field
        DF = driver.find_element(By.XPATH,
                                 '//*[@id="TabbedArea_4-panel-0"]/div/div/div/form/div[2]/div[2]/div[1]/label/div[1]/div/div/div/span/span')
        DF.click()
        time.sleep(2)

        MonthCalendar = driver.find_element(By.XPATH, '//div[@id="calendar-65"][1]')
        AllDates = MonthCalendar.find_elements(By.TAG_NAME, 'button')
        time.sleep(3)
        # print(len(AllDates))

        for date in AllDates:
            if date.text == "30":
                date.click()
                time.sleep(3)
                break

    def runtest3(self):
        baseUrl = 'https://www.expedia.com/'
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        # Click flights tab
        driver.find_element(By.LINK_TEXT, 'Flights').click()
        time.sleep(2)

        # Find & click departing field
        DF = driver.find_element(By.XPATH, '//button[contains(@aria-label,"Departing July 22, 2023") and contains(@data-name,"d1")]')
        DF.click()
        time.sleep(2)

        MonthCalendar = driver.find_element(By.XPATH, '//div[@data-stid="date-picker-month"][1]')
        AllDates = MonthCalendar.find_elements(By.TAG_NAME, 'button')
        # AllDates = driver.find_elements(By.XPATH, '//div[@data-stid="date-picker-month"][1]//tr//td')
        print(len(AllDates))

        for date in AllDates:
            if date.get_attribute('data-day') == '30':
                date.click()
                time.sleep(2)
                break


test = CalenderSelectionPractice()
test.runtest3()
