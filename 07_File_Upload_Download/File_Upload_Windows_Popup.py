from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.plupload.com/examples/")
driver.find_element(By.ID, 'uploader_browse').click()
time.sleep(5)

keyboard = Controller()

keyboard.type('C:\\Users\\Noor\\PycharmProjects\\SeleniumWDTutorial\\file_upload_download\\file.jpg')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
