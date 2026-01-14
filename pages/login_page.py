from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__username__ = (By.NAME, "username") #tuple (str, str)
        self.__password__ = (By.NAME, "password")
        self.__button__ = (By.CSS_SELECTOR, ".orangehrm-login-button")
        self.__error_message__ = (By.CSS_SELECTOR, ".oxd-alert--error")

    def input_username_field(self, username):
        return self.driver.find_element(*self.__username__).send_keys(username) #*self.__userName__ unpack tuple to 2 args

    def input_password_field(self, password):
        return self.driver.find_element(*self.__password__).send_keys(password)

    def clear_username_field(self):
        return self.driver.find_element(*self.__username__).clear()

    def clear_password_field(self):
        return self.driver.find_element(*self.__password__).clear()

    def click_login_button(self):
        return self.driver.find_element(*self.__button__).click()

    def press_enter_login_button(self):
        return self.driver.find_element(*self.__button__).send_keys(Keys.ENTER)

    def login_without_keyBoard(self, username, password):
        self.clear_username_field()
        self.input_username_field(username)
        self.clear_password_field()
        self.input_password_field(password)
        self.click_login_button()

    def login_with_enter_keyBoard(self, username, password):
        self.clear_username_field()
        self.input_username_field(username)
        self.clear_password_field()
        self.input_password_field(password)
        self.press_enter_login_button()

    def get_error_message(self):
        return self.driver.find_element(*self.__error_message__).text





