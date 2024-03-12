from selenium.webdriver.common.by import By
from src.Helper.BaseWrapper import BaseWrapper
from src.PageObjects.Login_page import LoginPage


class CommonPage(BaseWrapper):
    def navigate_to_url(self, url):
        self.driver.get(url)
        print(f"navigate to {url}")
        return LoginPage(self.driver)
