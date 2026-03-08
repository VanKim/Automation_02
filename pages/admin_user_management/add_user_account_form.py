from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.components.dropdown_component import DropdownComponents as Dropdown
from pages.components.input_component import InputComponents as Input
from pages.components.button_component import ButtonComponents as Button
from pages.components.autocomplete_component import AutocompleteComponents as AutocompleteField

class AddingUserForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # Have 3 Input fields: username, password, confirm password
        self.__input_fields__ = Input(self.driver)
        # Have 2 dropdowns: UserRole , Status dropdown
        self.__dropdown_fields__ = Dropdown(self.driver)
        # Employee Name - autocomplete
        self.__autocomplete_fields__ = AutocompleteField(self.driver)
        # Have 2 buttons: Cancel, Save
        self.__buttons__ = Button(self.driver)

    ####### Method #######
    def add_user(self, data):
        self.__dropdown_fields__.select_item_dropdown("User Role", data["infor"]["userRole"])
        self.__autocomplete_fields__.select_option_on_suggestion_list("Employee Name", data["infor"]["employeeName"])
        self.__dropdown_fields__.select_item_dropdown("Status", data["infor"]["status"])
        self.__input_fields__.enter_input_field("Username", data["infor"]["userName"])
        self.__input_fields__.enter_input_field("Password", data["password"])
        self.__input_fields__.enter_input_field("Confirm Password", data["confirmPassword"])
        self.__buttons__.click_button("Save")


