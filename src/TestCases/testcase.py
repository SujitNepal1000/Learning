import time
import pytest
from src.Helper.BrowserDriver import EnvironmentSetup
from src.PageObjects.CommonPage import CommonPage
from src.PageObjects.Login_page import LoginPage


class TestLogin:
    @pytest.fixture()
    def setup(self):
        self.driver = EnvironmentSetup().initialize_driver()
        yield
        self.driver.quit()

    def test_verify_login(self, setup):
        common_page = CommonPage(self.driver)
        login_page = common_page.navigate_to_url("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        login_page.enter_email("Admin")
        login_page.enter_pass("admin123")
        login_page.click_login()
        time.sleep(5)
