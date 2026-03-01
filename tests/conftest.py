from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from utils.config_reader import ConfigReader
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": ConfigReader.get_username(),
        "password": ConfigReader.get_password()
    }

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    
    if os.getenv("BROWSER"):
        browser = os.getenv("BROWSER")
    else:
        browser = "Chrome"

    print(f"Running test on browser: {browser}")

    # open browser
    match browser:
        case 'Chrome':
            driver = webdriver.Chrome(options=options)
        case 'Firefox':
            driver = webdriver.Firefox(options=options)
        case 'Edge':
            driver = webdriver.Edge(options=options)
        case 'Safari':
            driver = webdriver.Safari(options=options)
    #access base url
    base_url = ConfigReader.get_base_url()
    # input url on browser
    driver.get(base_url)
    #driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope ="function")
def login_driver(driver, credentials):
    login_page = LoginPage(driver)
    login_page.login_without_keyBoard(credentials["username"], credentials["password"])
    wait = WebDriverWait(driver, 15)
    wait.until(EC.url_contains("/dashboard"))
    return driver


