from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    first_button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn-primary").click()
    new_window = browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(x))
    second_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
