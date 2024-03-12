import os
from selenium import webdriver
from selenium.webdriver import Chrome
from dotenv import load_dotenv


class EnvironmentSetup:
    driver = None

    def initialize_driver(self):
        load_dotenv()
        options = webdriver.ChromeOptions()
        browser = os.getenv("BROWSER")
        wait = int(os.getenv("IMPLICIT_WAIT"))

        if browser == "chrome":
            driver = Chrome(options=options)
            driver.maximize_window()
            # Increase page load timeout to 10 seconds (adjust as needed)
            driver.set_page_load_timeout(10)
            return driver
        else:
            print("Invalid browser name provided in environment variables")

