from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
import os

def open_chrome_browser(browser, options, headless_flag):

    driver = None
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    return driver

def open_firefox_browser(browser, options_list, headless_flag):
    driver = None
    if headless_flag:
        options = FirefoxOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Firefox(options=options)
    else:
        driver = webdriver.Firefox()
    return driver

def open_edge_browser(browser, options, headless_flag):
    driver = None
    if headless_flag:
        options = EdgeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        driver = webdriver.Edge()
    return driver

def open_safari_browser(browser, options, headless_flag):
    driver = None
    if headless_flag:
        options = SafariOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Safari(options=options)
    else:
        driver = webdriver.Safari()
    return driver




