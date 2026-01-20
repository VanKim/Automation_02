import re
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class UserTable(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__total_number_user__ = (By.XPATH, "//span[contains(normalize-space(.), 'Records Found')]")
        self.__table_header_sort_alpha_username__ = (By.XPATH, "//div[@class='oxd-table-header'and @role='rowgroup']/div[@role='row']/div[@role='columnheader'][2]/descendant::i")
        self.__table_header_sort_alpha_user_role__ = (By.XPATH, "//div[@class='oxd-table-header'and @role='rowgroup']/div[@role='row']/div[@role='columnheader'][3]/descendant::i")
        self.__table_header_sort_alpha_employee_name__ = (By.XPATH, "//div[@class='oxd-table-header'and @role='rowgroup']/div[@role='row']/div[@role='columnheader'][4]/descendant::i")
        self.__table_header_sort_alpha_status__ = (By.XPATH, "//div[@class='oxd-table-header'and @role='rowgroup']/div[@role='row']/div[@role='columnheader'][5]/descendant::i")
        self.__add_button__ = (By.XPATH, "//button[normalize-space()='Add']")

        '''self.__action_delete__
        self.__action_edit__

        self.__single_checkbox__'''
        self.__checkbox_all__ = (By.XPATH, "//div[@class='oxd-table-header'and @role='rowgroup']/div[@role='row']/div[@role='columnheader'][1]")

    def get_total_number_user(self):
        self.find_element(self.__total_number_user__)
        text = self.text(self.__total_number_user__)
        #xử lý chuỗi để lấy số records
        if text =="No Records Found":
            return 0
        else:
            text = re.sub(r'[^0-9]', '', text)
            return text

    def click_on_add_button(self):
        self.find_element(self.__add_button__)
        self.click(self.__add_button__)