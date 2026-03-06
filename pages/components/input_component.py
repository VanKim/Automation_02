from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InputComponents(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ##### Method #####
    def get_xpath_input_by_label(self, label):
        return (By.XPATH, f"//label[normalize-space(.)='{label}']/ancestor::div[contains(@class,'oxd-grid-item--gutters')]//input")

    def enter_input_field(self, label, value):
        locator = self.get_xpath_input_by_label(label)
        self.send_keys(locator, value, True)

    def get_input_field(self, label):
        locator = self.get_xpath_input_by_label(label)
        return self.text(locator)
