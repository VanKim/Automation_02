from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
import os

# Configuration Browser Options
def config_chrome_options(headless_flag):
    options = ChromeOptions()
    options.add_argument('--lang=en-US')
    if headless_flag:
        options.add_argument('--headless=new')
    else:
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-extensions')
    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL"}
    )
    return options

def config_firefox_options(headless_flag):
    options = FirefoxOptions()
    options.add_argument('--lang=en-US')
    if headless_flag:
        options.add_argument('--headless')
    else:
        options.add_argument('--window-size=1920,1080')
        options.set_preference("dom.disable_open_during_load", False)
        options.profile.set_preference("extensions.enabledScopes", 0)
        options.profile.set_preference("xpinstall.signatures.required", False)
    return options

def config_edge_options(headless_flag):
    options = EdgeOptions()
    if headless_flag:
        options.add_argument('--headless=new')
    else:
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-extensions')
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": "en,en_US"}
    )
    options.set_capability(
        "goog:loggingPrefs",
        {"performance": "ALL"}
    )
    return options

def config_safari_options(headless_flag):
    options = SafariOptions()
    return options

# Open browser
def open_chrome_browser(driver, headless_flag):
    options = config_chrome_options(headless_flag)
    driver = webdriver.Chrome(options=options)
    # bật network tracking
    driver.execute_cdp_cmd("Network.enable", {})

    return driver

def open_firefox_browser(driver, headless_flag):
    options = config_firefox_options(headless_flag)
    driver = webdriver.Firefox(options=options)
    return driver

def open_edge_browser(driver, headless_flag):
    options = config_edge_options(headless_flag)
    driver = webdriver.Edge(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    return driver

def open_safari_browser(driver, headless_flag):
    options = config_safari_options(headless_flag)
    driver = webdriver.Safari(options=options)
    return driver




