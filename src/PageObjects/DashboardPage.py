from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.Helper.BaseWrapper import BaseWrapper


class DashboardPage(BaseWrapper):
    driver = None
    wait = None

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # web locators
    login_succ = (By.XPATH, "//h4[text()=' Your Activities ']")
    add_activity = (By.XPATH, "//button/span[text()='Add Activity']")
    manu_act = (By.XPATH, "//a[@id='add-activity-manually']")
    narrative_btn = (By.XPATH, "//input[@placeholder='Type narrative here']")
    sel_lang = (By.XPATH, "//input[@class='multiselect-search']")
    lang = (By.XPATH, "//li/span[text()='ne - Nepali']")
    act_id_btn = (By.XPATH, "//input[@placeholder='Type activity-identifier here']")
    save = (By.XPATH, "//button/span[text()='Save']")
    title = (By.XPATH,"//span[@class='max-w-[887px] text-sm']")
    err_narrative = (By.XPATH, "//span[text()='The narrative field is required.']")
    err_activity = (By.XPATH, "//span[text()='The activity identifier field is required.'] ")
    cancel = (By.XPATH, "//span[text()='Cancel']")

    def verify_login_success_msg(self):
        try:
            login_success_message = self.wait.until(
                expected_conditions.visibility_of_element_located(self.login_succ))
            assert login_success_message.is_displayed()
        except NoSuchElementException:
            print("No valid element found on the page.")
            raise NoSuchElementException('Test case Failed')

    def click_add_activity_btn(self):
        self.click_element(self.add_activity)

    def click_add_activity_manu(self):
        self.click_element(self.manu_act)

    def enter_nar(self,narrative):
        self.enter_narrative(self.narrative_btn, narrative)

    def select_lang(self,narrative):
        self.enter_language(self.sel_lang, narrative)

    def click_lang_btn(self):
        self.click_element(self.lang)

    def enter_act_identi(self,narrative):
        self.enter_identifier(self.act_id_btn, narrative)

    def click_save_btn(self):
        self.click_element(self.save)

    def click_cancel_btn(self):
        self.click_element(self.cancel)

    def verify_title(self, expected_id):
        try:
            groups_title = self.wait.until(
                expected_conditions.visibility_of_element_located(self.title))
            assert groups_title.is_displayed()
        except NoSuchElementException:
            print("No users page does not exist.")
            raise NoSuchElementException("Test case Failed")

    def verify_narrative_error_msg(self):
        try:
            login_success_message = self.wait.until(
                expected_conditions.visibility_of_element_located(self.err_narrative))
            assert login_success_message.is_displayed()
        except NoSuchElementException:
            print("No valid element found on the page.")
            raise NoSuchElementException('Test case Failed')

    def verify_activity_error_msg(self):
        try:
            login_success_message = self.wait.until(
                expected_conditions.visibility_of_element_located(self.err_activity))
            assert login_success_message.is_displayed()
        except NoSuchElementException:
            print("No valid element found on the page.")
            raise NoSuchElementException('Test case Failed')

    def verify_cancel(self):
        cancel_title = self.wait.until(expected_conditions.visibility_of_element_located(self.login_succ))
        assert cancel_title.is_displayed()



