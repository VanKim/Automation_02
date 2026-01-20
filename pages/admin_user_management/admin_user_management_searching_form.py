from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchingForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__username__ = (By.XPATH, "//label[.='Username']/../../descendant::input")
        self.__user_role__ = (By.XPATH, "//label[.='User Role']/../../descendant::div[@class='oxd-select-text-input']")
        self.__user_role_toggle__ = (By.XPATH, "//label[.='User Role']/../..//descendant::i")
        self.__employee_name__ = (By.XPATH, "//label[.='Employee Name']/../../descendant::input")
        self.__status__ = (By.XPATH, "//label[.='Status']/../../descendant::div[@class='oxd-select-text-input']")
        self.__status_toggle__ = (By.XPATH, "//label[.='Status']/../..//descendant::i")
        self.__reset_button__ = (By.XPATH, "///button[normalize-space()='Reset']")
        self.__search_button__ = (By.XPATH, "//button[normalize-space()='Search']")

    def select_user_role_dropdown(self, user_role_item):
        self.find_element(self.__user_role_toggle__)
        self.click(self.__user_role_toggle__)
        self.select_value_custom_dropdown((By.XPATH, f"//label[.='User Role']/../..//descendant::div[@role='listbox']//*[normalize-space()='{user_role_item}']"))

    def get_user_role_item(self):
        return self.text(self.__user_role__)

    def select_status_dropdown(self, status):
        self.find_element(self.__status_toggle__)
        self.click(self.__status_toggle__)
        self.select_value_custom_dropdown((By.XPATH, f"//label[.='Status']/../..//descendant::div[@role='listbox']//*[normalize-space()='{status}']"))

    def get_status_item(self):
        return self.text(self.__status__)

    def input_employee_name(self, employee_name):
        self.find_element(self.__employee_name__)
        self.send_keys(self.__employee_name__, employee_name)

    def get_employee_name(self):
        return self.text(self.__employee_name__)

    def click_on_reset_button(self):
        self.find_element(self.__reset_button__)
        self.click(self.__reset_button__)

    def click_on_search_button(self):
        self.find_element(self.__search_button__)
        self.click(self.__search_button__)