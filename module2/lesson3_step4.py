from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    first_button = browser.find_element(By.CLASS_NAME, "btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)
    input = browser.find_element(By.ID, "answer").send_keys(result)
    second_button = browser.find_element(By.CLASS_NAME, "btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
