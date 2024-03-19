from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseWrapper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def enter_username(self, locator, text_input):
        element = self.driver.find_element(*locator)
        element.send_keys(text_input)

    def enter_pwd(self, locator, text_input):
        element = self.driver.find_element(*locator)
        element.send_keys(text_input)

    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def enter_narrative(self, locator, text_input):
        element = self.driver.find_element(*locator)
        element.send_keys(text_input)

    def enter_language(self, locator, text_input):
        element = self.driver.find_element(*locator)
        element.send_keys(text_input)

    def enter_identifier(self, locator, text_input):
        element = self.driver.find_element(*locator)
        element.send_keys(text_input)

    def error_message(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
