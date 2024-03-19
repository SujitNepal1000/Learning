import time
import pytest
from src.Helper.BrowserDriver import EnvironmentSetup
from src.PageObjects.CommonPage import CommonPage
from src.TestData.test_env_data import data


class TestLogin:
    @pytest.fixture()
    def setup(self):
        self.driver = EnvironmentSetup().initialize_driver()
        yield
        self.driver.quit()

    def test_verify_login(self, setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email(data["user_email"])
        login_page.enter_pass(data["user_pwd"])
        login_page.click_login()
        login_page.verify_login_page()
        assert "activities" in self.driver.current_url.lower(), "Login failed. Dashboard not reached."
        print("Logged in successfully!")

    def test_verify_invalid_email(self, setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email(data["wrong_email"])
        login_page.enter_pass(data["user_pwd"])
        login_page.click_login()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.wrong_cred)
        assert error_message_element.is_displayed()
        print("Please enter correct credentials")

    def test_verify_invalid_password(self, setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email(data["user_email"])
        login_page.enter_pass(data["wrong_pwd"])
        login_page.click_login()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.wrong_cred)
        assert error_message_element.is_displayed()
        print("Please enter correct credentials")

    def test_verify_empty_credentials(self,setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email("")
        login_page.enter_pass("")
        login_page.click_login()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.empty_cred)
        assert error_message_element.is_displayed()
        print("Please enter username and password")

    def test_verify_empty_username(self,setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email("")
        login_page.enter_pass(data["wrong_pwd"])
        login_page.click_login()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.empty_username)
        assert error_message_element.is_displayed()
        print("Please enter username")

    def test_verify_empty_password(self,setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.enter_email(data["user_email"])
        login_page.enter_pass("")
        login_page.click_login()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.empty_password)
        assert error_message_element.is_displayed()
        print("Please enter password")

    def test_verify_reset(self, setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url(data["url"])
        time.sleep(5)
        login_page.click_reset()
        login_page.click_reset_email(data["reset_email"])
        time.sleep(2)
        login_page.click_send_btn()
        time.sleep(5)
        error_message_element = login_page.error_message(login_page.email_send)
        assert error_message_element.is_displayed()
        print("Email successfully send")


