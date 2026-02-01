from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (StaleElementReferenceException, ElementClickInterceptedException)

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def text(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def send_keys(self, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        try:
            self.wait_for_element_clickable(locator).click()
        except (StaleElementReferenceException, ElementClickInterceptedException):
            self.wait_for_element_clickable(locator).click()
        
    def wait_for_element_clickable(self, locator, timeout = 10):
         wait = WebDriverWait(self.driver, timeout)
         return wait.until(EC.element_to_be_clickable(locator))
        
    def select_drop_down_by_text(self, locator, value):
        element = Select(self.find_element(locator))
        element.select_by_visible_text(value)
    
    def select_drop_down_by_index(self, locator, index):
        element = Select(self.find_element(locator))
        element.select_by_index(index)

    def select_value_custom_dropdown(self, locator):
        self.find_element(locator)
        self.click(locator)
    
       