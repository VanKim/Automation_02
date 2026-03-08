import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 40)
    print(f'[DEBUG]\n\nCURRENT URL{login_driver.current_url}\n\n')
    locator = (By.XPATH, "//a[contains(@href, 'admin/viewAdminModule')]")
    admin_page = wait.until(
        EC.presence_of_element_located(locator)
    )
    admin_page.click()
    print(f"\n\n\n\n[INFO1:] JFGKFBKGJBDKFBGKDB {admin_page.get_attribute("outerHTML")}\n\n\n\n")
    admin_page = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@href, 'admin/viewAdminModule')]")
        )
    )
    admin_page.click()
    print("\n\n\n\n[INFO2:] JFGKFBKGJBDKFBGKDB\n\n\n\n")
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    print("\n\n\n\n[INFO3:] JFGKFBKGJBDKFBGKDB\n\n\n\n")

    return login_driver