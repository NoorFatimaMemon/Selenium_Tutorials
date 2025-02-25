from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():

    def runtest(self):
        baseurl = 'https://www.letskodeit.com/'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        # Login (How to click and type on a web element)
        driver.find_element(By.XPATH, '//a[contains(@href,"/login")]').click()
        time.sleep(3)

        UserID = driver.find_element(By.XPATH, '//input[@placeholder="Email Address"]')
        UserID.send_keys('noormemon457@gmail.com')

        Password = driver.find_element(By.XPATH, '//input[@id="login-password"]')
        Password.send_keys('NoorMemon15')
        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(@type,"button") and contains(@class,"btn btn-default btn-block btn-md dynamic-button") and contains(text(), "Login")]').click()

        # Search for ALL COURSES OPTION
        driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/ul/li[2]/a').click()

        # Search for courses
        SearchElement = driver.find_element(By.XPATH, '//input[contains(@class,"form-control find-input dynamic-text") and contains(@id, "search")]')
        SearchElement.send_keys('Selenium WebDriver With Python')
        driver.find_element(By.XPATH, '//*[@id="search"]/div/button').click()         #Hit Search Button
        time.sleep(3)

        #Choose the desired course
        Course_1 = '//h4[contains(text(), "{0}")]'
        CourseLocator = Course_1.format('Selenium WebDriver With Python 3.x')

        driver.find_element(By.XPATH, CourseLocator).click()
        time.sleep(2)

test = DynamicXpathFormat()
test.runtest()
