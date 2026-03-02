
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
import os

# Configuration Browser Options
def config_chrome_options(options_list):
    options = ChromeOptions()
    for option in options_list:
        options.add_argument(option)
    return options

def config_firefox_options(options_list):
    options = FirefoxOptions()
    for option in options_list:
        options.add_argument(option)
    return options

def config_edge_options(options_list):
    options = EdgeOptions()
    for option in options_list:
        options.add_argument(option)
    return options

def config_safari_options(options_list):
    options = SafariOptions()
    for option in options_list:
        options.add_argument(option)
    return options

# Open browser
def open_chrome_browser(driver, options_list):
    options = config_chrome_options(options_list)
    driver = webdriver.Chrome(options=options)
    return driver

def open_firefox_browser(driver, options_list):
    options = config_firefox_options(options_list)
    driver = webdriver.Firefox(options=options)
    return driver

def open_edge_browser(driver, options_list):
    options = config_edge_options(options_list)
    driver = webdriver.Edge(options=options)
    return driver

def open_safari_browser(driver, options_list):
    options = config_safari_options(options_list)
    driver = webdriver.Safari(options=options)
    return driver




