from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

PRODUCT = "https://www.saturn.de/de/product/_sony-playstation%C2%AE5-2661938.html"
# PRODUCT = "https://www.saturn.de/de/product/_sony-dualsense™-2681392.html"
USERNAME = "user@email.com"
PASSWORD = "someFancyPassword"


def click_button(button_text):
    try:
        element = driver.find_element(By.XPATH, f'//button[text()="{button_text}"]')
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)
        return True
    except NoSuchElementException:
        return False


def login_mms(username, password):
    driver.find_element_by_id("mms-login-form__email").send_keys(username)
    driver.find_element_by_id("mms-login-form__password").send_keys(password)
    driver.find_element_by_id("mms-login-form__login-button").click()
    time.sleep(3)


driver = webdriver.Chrome()
driver.get(PRODUCT)
while True:
    click_button("Alle zulassen")
    if click_button("In den Warenkorb"):
        break
    driver.refresh()
click_button("Nein, danke")
click_button("Zum Warenkorb")
click_button("Zur Kasse gehen")
login_mms(USERNAME, PASSWORD)
click_button("Weiter")
click_button("Fortfahren und bezahlen")
