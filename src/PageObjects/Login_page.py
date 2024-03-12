from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.Helper.BaseWrapper import BaseWrapper


class LoginPage(BaseWrapper):
    locator_email = (By.XPATH, "//input[@name='username']")
    locator_pass = (By.XPATH, "//input[@name='password']")
    locator_login_btn = (By.XPATH, "//button[@type='submit']")

    def enter_email(self, email):
        self.enter_username(self.locator_email, email)

    def enter_pass(self, pwd):
        self.enter_pwd(self.locator_pass, pwd)

    def click_login(self):
        self.click_element(self.locator_login_btn)
