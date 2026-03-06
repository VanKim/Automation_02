from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import json
from utils.wait_for_api import *
from pages.components.button_component import ButtonComponents as Button
from pages.components.input_component import InputComponents as Input

class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
       ###### Searching form layout
        # username input field
        self.__input_fields__ = Input(self.driver)
        self.__user_role__ = (By.XPATH, "//label[.='User Role']/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]//div[@class ='oxd-select-text-input']")
        self.__user_role_list__ = (By.XPATH, "//label[.='User Role']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//div[contains(@role, 'listbox')]/div[contains(@role, 'option')]")
        self.__user_role_toggle__ = (By.XPATH, "//label[.='User Role']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//i")
        self.__employee_name__ = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
        self.__autocomplete_employee__ = (By.XPATH, "//label[.='Employee Name']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//div[contains(@role, 'listbox')]/div[contains(@role, 'option')]")
        self.__status___ = (By.XPATH,"//label[.='Status']/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]//div[@class ='oxd-select-text-input']")
        self.__status_list__ = (By.XPATH, "//label[.='Status']/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]//div[contains(@role, 'listbox')]/div[contains(@role, 'option')]")
        self.__status_toggle__ = (By.XPATH, "//label[.='Status']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//i")
        # Have 3 buttons: Reset, Search, Add
        self.__buttons__ = Button(self.driver)

        ###### User list table
        self.__total_records__ = (By.XPATH, "//div[@class='orangehrm-paper-container']/descendant::span")
        # Header table
        self.__header_table__ = (By.XPATH, "//div[@role='table']/div[@class='oxd-table-header']//div[@role='columnheader']")
        self.__header_sort_button__ = (By.XPATH, ".//div[@class='oxd-table-header-sort']")
        self.__header_sort_dropdown__ = (By.XPATH, ".//div[@class='oxd-table-header-sort-dropdown']/ul/li")
        # Body table
        self.__body_table__ = (By.XPATH, "//div[@role='table']/div[@class='oxd-table-body']//div[@class='oxd-table-card']")
        self.__data_cell__ = (By.XPATH, ".//div[contains(@class, 'oxd-table-cell')]")
        self.__checkbox_col__ = (By.XPATH, ".//div[@class='oxd-table-card-cell-checkbox']//input")
        self.__data_col__ = (By.XPATH, ".//div")
        self.__delete_action__ = (By.XPATH, ".//div[@class ='oxd-table-cell-actions']/button/i[@class='oxd-icon bi-trash']")
        self.__edit_action__ = (By.XPATH, ".//div[@class ='oxd-table-cell-actions']/button/i[@class='oxd-icon bi-pencil-fill']")
        self.__confirm_popup_yes_button__ = (By.XPATH, "(.//div[contains(@class, 'orangehrm-dialog-popup')]/div[contains(@class, 'orangehrm-modal-footer')]/button)[2]")
        self.__confirm_popup_no_button__ = (By.XPATH, "(.//div[contains(@class, 'orangehrm-dialog-popup')]/div[contains(@class, 'orangehrm-modal-footer')]/button)[1]")

        ###### Navigation Header


    ##### Method #######
    # Group methods of searching form
    def get_username(self):
        return self.__input_fields__.get_input_field("Username")

    def select_user_role_dropdown(self, user_role_item):
        self.click(self.__user_role_toggle__)
        self.select_value_custom_dropdown(self.__user_role_list__, user_role_item)

    def get_user_role(self):
        return self.text(self.__user_role__)

    def select_status_dropdown(self, status_item):
        self.click(self.__status_toggle__)
        self.select_value_custom_dropdown(self.__status_list__, status_item)

    def get_status(self):
        return self.text(self.__status___)

    def input_employee_name(self, keyword):
        self.send_keys(self.__employee_name__, keyword, True)
        if keyword != '':
            self.select_value_autocomplete_list(self.__autocomplete_employee__)

    def get_employee_name(self):
        return self.text(self.__employee_name__)

    def search_user_account(self, username, user_role, employee_name, status):
        self.__input_fields__.enter_input_field("Username")
        self.select_user_role_dropdown(user_role)
        self.input_employee_name(employee_name)
        self.select_status_dropdown(status)
        self.__buttons__.click_button("Search")

    def reset_search_form(self, username, user_role, employee_name, status):
        self.__input_fields__.enter_input_field("Username")
        self.select_user_role_dropdown(user_role)
        self.input_employee_name(employee_name)
        self.select_status_dropdown(status)
        self.__buttons__.click_button("Reset")

    # User Account list from API
    def get_response_user_account_list(self, keyword):
        return wait_for_get_api(self.driver, keyword)

    def get_total_records_label(self):
        total_records_label = self.text(self.__total_records__)
        total_records_label = ''.join((i for i in total_records_label if i.isdigit()))
        total_records_label = 0 if total_records_label == '' else int(total_records_label)
        return total_records_label

    def get_user_account_list_table(self):
        return  self.find_elements(self.__body_table__)

    def get_data_for_a_user_account_record(self, record_row):
        record_cells = record_row.find_elements(*self.__data_cell__)
        data_record = {
            "userName": record_cells[1].find_element(*self.__data_col__).text,
            "userRole": record_cells[2].find_element(*self.__data_col__).text,
            "employeeName": record_cells[3].find_element(*self.__data_col__).text,
            "status": record_cells[4].find_element(*self.__data_col__).text
        }
        return data_record

    def delete_action(self, record_row):
        record_row.click(*self.__delete_action__)

    def edit_action(self, record_row):
        record_row.click(*self.__edit_action__)

    def add_button(self):
        self.__buttons__.click_button("Add")

    # Navigation Header
