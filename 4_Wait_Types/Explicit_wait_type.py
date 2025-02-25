from traceback import print_stack
from Utilities.HandyWrappers import HandyWrappers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    def WaitForElement(self, Locator, LocatorType='id', timeout_1=10, poll_frequency=0.6):
        element = None
        try:
            self.driver.implicit_wait(2)
            ByType = self.hw.getByType(LocatorType)
            print("Waiting for maximum :: " + str(timeout_1) + " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchFrameException,
                                                     ElementNotSelectableException,
                                                     ElementNotVisibleException])
            element = wait.until(EC.element_to_be_clickable((ByType, Locator)))

            print("Element appeared on the web page!")

        except:
            print("Element not appeared on the web page!")
            print_stack()
        self.driver.implicit_wait(3)
        return element
