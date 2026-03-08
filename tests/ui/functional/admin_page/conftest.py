import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 30)
    # wait dashboard load
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space(.)='Admin']")
        )
    )

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[normalize-space(.)='Admin']")
    )).click()
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    return login_driver