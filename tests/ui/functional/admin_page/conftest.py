import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 50)
    print(f'[DEBUG]\n\nCURRENT URL{login_driver.current_url}\n\n')
    locator = (By.XPATH, "//a[contains(@href, 'admin/viewAdminModule')]")
    print(f'[DEBUG]\n\nPAGE SOURCE: {login_driver.page_source}\n\n')
    print("Admin exist:", login_driver.find_elements(*locator))
    admin_page = wait.until(EC.element_to_be_clickable(locator))
    #print(f"\n\n\n\n[INFO2:] JFGKFBKGJBDKFBGKDB{admin_page}\n\n\n\n")
    #admin_page.click()
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    #print("\n\n\n\n[INFO3:] JFGKFBKGJBDKFBGKDB\n\n\n\n")

    return login_driver