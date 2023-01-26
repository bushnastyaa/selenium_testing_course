from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    for elem_name in ["firstname", "lastname", "email"]:
        browser.find_element(By.NAME, elem_name).send_keys(elem_name)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Document.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
