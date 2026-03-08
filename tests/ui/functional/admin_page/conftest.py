import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def admin_page_driver(login_driver):
    wait = WebDriverWait(login_driver, 200)
    print(f'[DEBUG]\n\nCURRENT URL{login_driver.current_url}\n\n')
    locator = (By.XPATH, "//nav[@role='navigation']//*[text()='Admin']")
    admin_page = wait.until(EC.presence_of_element_located(locator))
    print(f'[DEBUG]\n\nPAGE SOURCE: {login_driver.page_source}\n\n')
    print(f'[DEBUG]\n\nPAURCE: {admin_page.get_attribute('outerHTML')}\n\n')
    admin_page = wait.until(EC.element_to_be_clickable(locator)).click()
    wait.until(EC.url_contains("/admin/viewSystemUsers"))
    print(f'[DEBUG]\n\nCURRENT URL{login_driver.current_url}\n\n')
    return login_driver