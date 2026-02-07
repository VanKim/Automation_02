from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__username__ = (By.NAME, "username")
        self.__password__ = (By.NAME, "password")
        self.__button__ = (By.CSS_SELECTOR, ".orangehrm-login-button")
        self.__error_message__ = (By.CSS_SELECTOR, ".oxd-alert--error")

    def input_username_field(self, username):
        self.send_keys(self.__username__,username, clear = True) #*self.__userName__ unpack tuple to 2 args

    def input_password_field(self, password):
        self.send_keys(self.__password__,password, clear = True)

    def click_login_button(self):
        self.click(self.__button__)

    def press_enter_login_button(self):
        self.send_keys(self.__button__,Keys.ENTER, clear = False)

    def login_without_keyBoard(self, username, password):
        self.input_username_field(username)
        self.input_password_field(password)
        self.click_login_button()

    def login_with_enter_keyBoard(self, username, password):
        self.input_username_field(username)
        self.input_password_field(password)
        self.press_enter_login_button()

    def get_error_message(self):
        return self.find_element(self.__error_message__).text





