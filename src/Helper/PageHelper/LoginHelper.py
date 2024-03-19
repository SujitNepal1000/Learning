from src.PageObjects.Login_page import LoginPage, DashboardPage


class LoginHelper(LoginPage):

    def perform_successfull_login(self):
        self.verify_login_page()