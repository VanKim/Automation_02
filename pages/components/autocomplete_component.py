from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import json
from utils.wait_for_api import *

class AutocompleteComponents(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ##### Method #####
    def get_xpath_keyword_autocomplete(self, label):
        return (By.XPATH, f"//label[.='{label}']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//input")

    def get_keyword_autocomplete_field(self, label):
        locator = self.get_xpath_keyword_autocomplete(label)
        return self.text(locator)

    def get_xpath_suggesstion_list(self, label):
        return (By.XPATH, f"//label[.='{label}']/ancestor::div[contains(@class, 'oxd-input-field-bottom-space')]//div[contains(@role, 'listbox')]/div[contains(@role, 'option')]")

    def select_option_on_suggestion_list(self, label, keyword):
        if keyword != '':
            locator = self.get_xpath_keyword_autocomplete(label)
            locators = self.get_xpath_suggesstion_list(label)
            self.send_keys(locator, keyword, True)
            self.select_value_autocomplete_list(locators)