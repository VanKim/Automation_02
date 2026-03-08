import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 30)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space(.)='Admin']")
    )).click()
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    return login_driver