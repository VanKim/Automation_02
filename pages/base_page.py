from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException)

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

    def find_elements(self, locator, timeout=20):
        wait = WebDriverWait(self.driver, timeout)
        print(f'[DEBUG]LOCATOR: {locator}')
        try:
            elements = wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            elements = wait.until(EC.visibility_of_all_elements_located(locator))
        else:
            return elements

    def send_keys(self, locator, value, clear, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        if clear:
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

    def select_value_custom_dropdown(self, locator, value ):
        value_list = self.find_elements(locator)
        element = None
        for item in value_list:
            if item.text == value:
                element = item
                self.click(element)
                break

    def select_value_autocomplete_list(self, locator):
        WebDriverWait(self.driver, 12).until(
            EC.invisibility_of_element_located(
                (By.XPATH, "//div[@role='option'][contains(.,'Searching')]")
            )
        )
        employee_name_list = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )
        self.click(employee_name_list[0])

    def current_url(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    def wait_for_element_visibile(self, locator, timeout = 10):
         wait = WebDriverWait(self.driver, timeout)
         return wait.until(EC.visibility_of_all_elements_located(locator))

