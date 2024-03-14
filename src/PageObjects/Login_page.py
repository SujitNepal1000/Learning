from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.Helper.BaseWrapper import BaseWrapper


class LoginPage(BaseWrapper):
    locator_email = (By.XPATH, "//input[@id='username' ]")
    locator_pass = (By.XPATH, "//input[@id='password' ]")
    locator_login_btn = (By.XPATH, "//button[@id='btn'] ")
    wrong_cred = (By.XPATH, "//div/span[text()='These credentials do not match our records.']")
    empty_cred = (By.XPATH, "//span[@class='error text-xs']")
    empty_username = (By.XPATH, "//span[text()='The username field is required.']")
    empty_password = (By.XPATH, "//span[text()='The password field is required.']")
    reset_btn = (By.XPATH, "//a[text()='Reset.']")
    re_email = (By.XPATH, "//input[@placeholder='Enter your email address']")
    reset_error = (By.XPATH, "//div/span[@class='error']")
    send_mail = (By.XPATH, "//button[@type='submit']")
    email_send = (By.XPATH, "//h2[text()='Password Recovery']")

    def enter_email(self, email):
        self.enter_username(self.locator_email, email)

    def enter_pass(self, pwd):
        self.enter_pwd(self.locator_pass, pwd)

    def click_login(self):
        self.click_element(self.locator_login_btn)

    def error_message(self, locator):
        return self.driver.find_element(*locator)

    def click_reset(self):
        self.click_element(self.reset_btn)

    def click_reset_email(self, reset_email):
        self.enter_username(self.re_email, reset_email)

    def click_send_btn(self):
        self.click_element(self.send_mail)


