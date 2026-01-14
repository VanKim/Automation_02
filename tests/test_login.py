from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

class TestLoginPage:

    def test_login_successfully_click_button(self, driver, credentials):
        login_page = LoginPage(driver)
        login_page.login_without_keyBoard(credentials["username"], credentials["password"])
        dashboard_page =DashboardPage(driver)
        assert dashboard_page.get_header() == "Dashboard"

    def test_login_successfully_enter_keyboard(self, driver, credentials):
        login_page = LoginPage(driver)
        login_page.login_with_enter_keyBoard(credentials["username"], credentials["password"])
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.get_header() == "Dashboard"

    def test_login_failure_invalid_username(self, driver, username="Admin1", password="admin123"):
        login_page = LoginPage(driver)
        login_page.login_without_keyBoard(username,password)
        assert login_page.get_error_message() == "Invalid credentials"

    def test_login_failure_password_wrong(self, driver, username="Admin1", password="admin123"):
        login_page = LoginPage(driver)
        login_page.login_without_keyBoard(username, password)
        assert login_page.get_error_message() == "Invalid credentials"
