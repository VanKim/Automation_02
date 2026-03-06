from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ButtonComponents(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ##### Method #####
    def get_xpath_button_by_label(self, label):
        return  (By.XPATH, f"//button[normalize-space()='{label}']")

    def click_button(self, label):
        locator = self.get_xpath_button_by_label(label)
        self.click(locator)
