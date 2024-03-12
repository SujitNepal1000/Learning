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
        time.sleep(5)
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
        error_message_element = login_page.error_message(login_page.wrong_username)
        assert error_message_element.is_displayed()
        print("Please enter correct credentials")

