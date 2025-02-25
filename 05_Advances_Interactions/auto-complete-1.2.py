from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseURL = 'https://www.goibibo.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
driver.implicitly_wait(5)
PartialText = 'Kara'
CompleteText = 'Karachi, Pakistan '

driver.find_element(By.XPATH, '//div[contains(@class,"sc-12foipm-16 dwhdnN fswFld") and contains(@style,"width: 260px;")]').click()

InputElement = driver.find_element(By.XPATH, '//input[@type="text"]')
InputElement.send_keys(PartialText)
time.sleep(2)

AutoList = driver.find_element(By.ID, 'autoSuggest-list')
htmlText = AutoList.get_attribute("innerHTML")
# print(htmlText)

liElements = AutoList.find_elements(By.TAG_NAME, 'li')
time.sleep(2)

for element in liElements:
    if CompleteText in element.text:
        element.click()
        break

time.sleep(2)
driver.quit()
