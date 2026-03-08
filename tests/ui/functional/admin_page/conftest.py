import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 15)
    print(f'[DEBUG]\n\nCURRENT URL{login_driver.current_url}\n\n')
    try:
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space(.)='Admin']")
            )
        )

        admin_menu = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[normalize-space(.)='Admin']")
            )
        )
        admin_menu.click()
        wait.until(EC.url_contains("/admin/viewSystemUsers"))
    except TimeoutException:
        login_driver.save_screenshot("report/debug_admin.png")

    return login_driver