from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseURL = 'https://www.google.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
driver.implicitly_wait(5)
PartialText = 'Ana'
CompleteText = 'Ana de Armas'

InputElement = driver.find_element(By.XPATH, '//textarea[@id="APjFqb"]')
InputElement.send_keys(PartialText)
time.sleep(2)

AutoList = driver.find_element(By.CLASS_NAME, 'G43f7e')
htmlText = AutoList.get_attribute("innerHTML")
# print(htmlText)

liElements = AutoList.find_elements(By.TAG_NAME, 'li')
time.sleep(2)

for element in liElements:
    # print(element.text)
    if CompleteText in element.text:
        element.click()
        break

time.sleep(2)
driver.quit()
