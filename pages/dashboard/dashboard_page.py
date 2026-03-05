from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__header__ = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module")
        self.__title_page__ = (By.XPATH, "//head/title[normalize-space(.)=='OrangeHRM']")

    def get_header(self):
        return self.find_element(self.__header__).text