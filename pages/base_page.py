from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    # def click(self, locator):
    #     element = self.wait_for_element_clickable(locator)
    #     try:
    #         element.click()
    #     except NoSuchElementException:
    #         element = self.wait_for_element_clickable()
    #         element.click()
        
    # def wait_for_element_clickable(self, locator, timeout = None):
        
    def select_drop_down_by_text(self, locator, value):
        element = Select(self.find_element(locator))
        return element.select_by_visible_text(value)
    
    def select_drop_down_by_id(self, locator, value):
        element = Select(self.find_element(locator))
        return element.select_by_index(value)
    
       