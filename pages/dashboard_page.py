from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.__header__ = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb-module")

    def get_header(self):
        return self.driver.find_element(*self.__header__).text