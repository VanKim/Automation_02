from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def


'''def test_form():
    driver = webdriver.Chrome()
    # input url on browser
    driver.get('https://the-internet.herokuapp.com/login')
    driver.maximize_window()
    #driver.implicitly_wait(10)
    sleep(5)
    driver.find_element(By.NAME, "username").send_keys("tomsmith")
    driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.TAG_NAME, "form").submit()
    assert driver.find_element(By.XPATH, "//h2").text == "Secure Area"
    driver.quit()'''

'''def test_switch_to_window():
    driver = webdriver.Chrome()
    # input url on browser
    driver.get('https://www.letskodeit.com/practice')
    driver.maximize_window()
    #driver.implicitly_wait(10)
    sleep(5)
    driver.find_element(By.ID, "openwindow").click()
    driver.switch_to.window(driver.window_handles[1])
    driver.maximize_window()
    sleep(5)
    driver.quit()'''

# def test_alert_accept_1():
#     driver = webdriver.Chrome()
#     # input url on browser
#     driver.get('https://www.letskodeit.com/practice')
#     driver.maximize_window()
#     #driver.implicitly_wait(10)
#     driver.find_element(By.ID, "alertbtn").click()
#     sleep(5)
#     driver.switch_to.alert.accept()
#     sleep(5)
#     driver.quit()


'''def test_alert_accept():
    driver = webdriver.Chrome()
    driver.get('https://www.letskodeit.com/practice')
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    # click the simple Alert button
    wait.until(EC.element_to_be_clickable((By.ID, "alertbtn"))).click()
    sleep(5)
    # wait for alert and accept it
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text  # optional: inspect or assert text
    alert.accept()
    sleep(5)
    # optional quick verification that alert was handled (no alert present)
    wait.until(lambda d: d.execute_script("return window.alert == undefined || typeof window.alert === 'function'"))
'''


'''def test_hover_main_item_2():
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/menu")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    main_item = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//a[normalize-space()='Main Item 2']")
    ))

    # perform hover
    ActionChains(driver).move_to_element(main_item).perform()
    sleep(5)
    # attempt to find the submenu element (two common structures)
    submenu = None
    try:
        submenu = driver.find_element(By.XPATH, "//a[normalize-space()='Main Item 2']/following-sibling::ul")
    except Exception:
        try:
            submenu = driver.find_element(By.XPATH, "//a[normalize-space()='Main Item 2']/../ul")
        except Exception:
            submenu = None

    assert submenu is not None and submenu.is_displayed()
    driver.quit()
'''