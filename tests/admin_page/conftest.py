import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    driver = login_driver
    wait = WebDriverWait(driver, 10)
    #login_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
    #wait.until(EC.url_contains("/admin_user_management"))
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space()='Admin']")
    )).click()
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    return driver