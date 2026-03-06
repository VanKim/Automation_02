from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DropdownComponents(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ##### Method #####
    def get_xpath_item_dropdown(self, label):
        return (By.XPATH, f"//label[.='{label}']/ancestor::div[contains(@class,'oxd-input-field-bottom-space')]//div[@class ='oxd-select-text-input']")
    def get_item_dropdown(self, label):
        locator = self.get_xpath_item_dropdown(label)
        return self.text(locator)

    def get_xpath_item_list_dropdown(self, label):
        return (By.XPATH, f"//label[.='{label}']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//div[contains(@role, 'listbox')]/div[contains(@role, 'option')]")
    def get_item_list_dropdown(self, label):
        locator = self.get_xpath_item_list_dropdown(label)
        return self.find_elements(locator)

    def get_xpath_dropdown_toggle(self, label):
        return (By.XPATH, f"//label[.='{label}']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//i")
    def select_item_dropdown(self, label, item):
        locator = self.get_xpath_dropdown_toggle(label)
        locators = self.get_xpath_item_list_dropdown(label)
        self.click(locator)
        self.select_value_custom_dropdown(locators, item)



