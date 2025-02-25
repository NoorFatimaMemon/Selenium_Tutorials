import time
from selenium import webdriver

class BrowseInteractions():

    def runtest(self):
        baseurl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)

        driver.maximize_window()                                    # Maximizing current window

        driver.get(baseurl)                                         # Loading web page

        title = driver.title                                        # Returning current page title
        print("Title of the current page is: " + title)

        currenturl = driver.current_url                             # current url of the loaded page
        print("Current url of the loaded page is: " + currenturl)
        time.sleep(5)

        driver.refresh()                                            # refreshing the browser first time
        print("Browser is refreshed for the first time")
        time.sleep(5)

        driver.get(driver.current_url)                              # refreshing the browser second time
        print("Browser is refreshed for the 2nd time")
        time.sleep(5)

        driver.get("https://www.letskodeit.com/courses")                #open other url
        time.sleep(5)

        currenturl = driver.current_url                             # current url of the loaded page
        print("Current url of the loaded page is: " + currenturl)

        driver.back()
        print("Go one step back in the browser")
        time.sleep(5)

        currenturl = driver.current_url                             # current url of the loaded page
        print("Current url of the loaded page is: " + currenturl)

        driver.forward()
        print("Go one step forward in the browser")
        time.sleep(3)

        currenturl = driver.current_url                             # current url of the loaded page
        print("Current url of the loaded page is: " + currenturl)

        pagesource = driver.page_source                             # finding page source
        print(pagesource)
        time.sleep(5)

        driver.close()
        #driver.quit()

x = BrowseInteractions()
x.runtest()
