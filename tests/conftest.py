from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
import os
from utils.browser_factory import *


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": ConfigReader.get_username(),
        "password": ConfigReader.get_password()
    }

@pytest.fixture(scope="function")
def driver():
    options_list = []
    headless_flag = False

    # Setup headless mode if test script is triggered from application_deploy.yaml else none
    if os.getenv("HEADLESS") == "True":
        headless_flag = True
        options_list.append('--headless=new')
    else:
        headless_flag = False

    # Receive browser type from application_deploy.yml else default: Chrome browser
    if os.getenv("BROWSER") is not None:
        browser = os.getenv("BROWSER")
    else:
        browser = "Chrome"

    # Open browser
    driver = None
    match browser:
        case 'Chrome':
            driver = open_chrome_browser(driver, options_list)
        case 'Firefox':
            driver = open_firefox_browser(driver, options_list)
        case 'Edge':
            driver = open_edge_browser(driver, options_list)
        case 'Safari':
            driver = open_safari_browser(driver, options_list)

    # Get cookies


    print(f"[DEBUG] Running test with BASE URL: {os.getenv("BASE_URL")}")
    # Receive BASE_URL from application_deploy.yml else get from testsetting.json
    base_url = None
    if os.getenv("BASE_URL"):
        base_url = os.getenv("BASE_URL")
    else:
        base_url = ConfigReader.get_base_url()

    # Access base_url on browser
    driver.get(base_url)
    yield driver
    # Close & delete Profile browser
    driver.quit()

@pytest.fixture(scope ="function")
def login_driver(driver, credentials):
    login_page = LoginPage(driver)
    login_page.login_without_keyBoard(credentials["username"], credentials["password"])
    wait = WebDriverWait(driver, 15)
    wait.until(EC.url_contains("/dashboard"))
    return driver


