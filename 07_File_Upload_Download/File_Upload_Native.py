import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.plupload.com/examples/")
driver.get('https://imgbb.com/upload')
driver.implicitly_wait(5)

# element = driver.find_element(By.ID, 'uploader_browse') Error: Message: element not interactable
# element = driver.find_element(By.CLASS_NAME, 'upload-box-queue content-width soft-hidden queueEmpty') Error
# element = driver.find_element(By.XPATH, '//div[@id="uploader_buttons"]/div/input')
element = driver.find_element(By.ID, 'anywhere-upload-input-camera')
element.send_keys('C:\\Users\\Noor\\Downloads\\file.jpg')
time.sleep(5)

"""driver.find_element(By.LINK_TEXT, 'Start Upload').click()
time.sleep(4)"""
