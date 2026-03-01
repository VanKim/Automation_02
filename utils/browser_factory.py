from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions
import os

def browser():

    print(f"[DEBUG] Running test on browser: {os.getenv("BROWSER")}")
    #Receive browser type from application_deploy.yml else default: Chrome browser
    #Setup headless mode if test script is triggered from application_deploy.yaml else none
    headless_flag = False
    if os.getenv("BROWSER"):
        browser = os.getenv("BROWSER")
        headless_flag = True
    else:
        browser = "Chrome"

    # Open browser
    driver = None
    match browser:
        case 'Chrome':
            if headless_flag:
                options = ChromeOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Chrome(options=options)
            else:
                driver = webdriver.Chrome()
        case 'Firefox':
            if headless_flag:
                options = FirefoxOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Firefox(options=options)
            else:
                driver = webdriver.Firefox()
        case 'Edge':
            if headless_flag:
                options = EdgeOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Edge(options=options)
            else:
                driver = webdriver.Edge()
        case 'Safari':
            if headless_flag:
                options = SafariOptions()
                options.add_argument("--headless=new")
                driver = webdriver.Safari(options=options)
            else:
                driver = webdriver.Safari()







