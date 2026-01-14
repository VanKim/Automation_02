import sys
import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def credentials():
    return {
        "username": ConfigReader.get_username(),
        "password": ConfigReader.get_password()
    }

@pytest.fixture
def driver():
    # open browser
    driver = webdriver.Chrome()
    base_url = ConfigReader.get_base_url()
    # input url on browser
    driver.get(base_url)
    driver.maximize_window()
    driver.implicitly_wait(ConfigReader.get_implicit())
    yield driver
    driver.quit()