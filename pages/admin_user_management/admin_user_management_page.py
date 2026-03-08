from time import sleep

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import json
from utils.wait_for_api import *
from pages.components.button_component import ButtonComponents as Button
from pages.components.input_component import InputComponents as Input
from pages.components.dropdown_component import DropdownComponents as Dropdown
from pages.components.autocomplete_component import AutocompleteComponents as Autocomplete

class AdminPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        ##### Searching form layout
        # username input field
        self.__input_field__ = Input(self.driver)
        # Dropdown: Status, User Role
        self.__dropdown__ = Dropdown(self.driver)
        # Autocomplete field: employee Name
        self.__autocomplete_field__ = Autocomplete(self.driver)
        # Have 3 buttons: Reset, Search, Add
        self.__button__ = Button(self.driver)

        ###### User list table layout
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

        ###### Navigation Header layout
        self.__navigation_tab_list__ = (By.XPATH, "//nav[@role='navigation' and @aria-label='Topbar Menu']/ul/li")
        self.__navigation_tab_name__ = (By.XPATH, ".//a | .//span")
        self.__option_list_nav_tab__ = (By.XPATH, ".//ul/li")
        self.__option_nav_tab__ = (By.XPATH, ".//a")
        self.__navigation_tab_toggle__ = (By.XPATH, ".//span/i")

    ##### Method #######
    # Group methods of searching form
    def get_username(self):
        return self.__input_field__.get_input_field("Username")

    def get_user_role(self):
        return self.__dropdown__.get_item_dropdown("User Role")

    def get_status(self):
        return self.__dropdown__.get_item_dropdown("Status")

    def get_employee_name(self):
        return self.__autocomplete_field__.get_keyword_autocomplete_field("Employee Name")

    def search_user_account(self, username, user_role, employee_name, status):
        self.__input_field__.enter_input_field("Username", username)
        self.__dropdown__.select_item_dropdown("User Role", user_role)
        self.__autocomplete_field__.select_option_on_suggestion_list("Employee Name", employee_name)
        self.__dropdown__.select_item_dropdown("Status", status)
        self.__button__.click_button("Search")

    def reset_search_form(self, username, user_role, employee_name, status):
        self.__input_field__.enter_input_field("Username", username)
        self.__dropdown__.select_item_dropdown("User Role", user_role)
        self.__autocomplete_field__.select_option_on_suggestion_list("Employee Name", employee_name)
        self.__dropdown__.select_item_dropdown("Status", status)
        self.__button__.click_button("Reset")

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
        record_row.find_element(*self.__delete_action__).click()

    def confirm_delete_popup(self, flag):
        if flag:
            self.click(self.__confirm_popup_yes_button__)
        else:
            self.click(self.__confirm_popup_no_button__)

    def edit_action(self, record_row):
        record_row.click(*self.__edit_action__)

    def add_button(self):
        self.__button__.click_button("Add")

    # Navigation Header
    def get_navigation_list(self):
        print(f'[DEBUG]self.__navigation_tab_list__: {self.__navigation_tab_list__}\n\n')

        nav_list = self.find_elements(self.__navigation_tab_list__)
        print(f'[DEBUG]nav_list method: {nav_list}\n\n')
        return nav_list
        #return self.find_elements(self.__navigation_tab_list__)

    # Get webElement for a navigation tab
    def get_navigation_tab(self, nav_list, nav_name):
        for i in nav_list:
            element_name = i.find_element(*self.__navigation_tab_name__)
            if element_name.text.strip() == nav_name:
                return i
        return None

    # Get option list of a navigation tab
    def get_option_list_of_nav_tab(self, nav_tab):
        try:
            return nav_tab.find_elements(*self.__option_list_nav_tab__)
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    def open_option_list_nav_tab(self, nav_tab):
        try:
            nav_tab.find_element(*self.__navigation_tab_toggle__)
            nav_tab.click()
        except (NoSuchElementException, StaleElementReferenceException):
            return None

    # Action for navigation tabs don't have any options
    def click_on_navigation_tab(self, nav_tab):
        nav_tab.click()

    # Action for navigation tabs have at least one option
    def select_option_of_a_navigation_tab(self, options, option_name):
        for i in options:
            element = i.find_element(*self.__option_nav_tab__)
            if element.get_attribute("innerHTML").strip() == option_name:
                element.click()
                break

    def back(self):
        self.driver.back()

    def get_current_url(self):
        return self.driver.current_url
