from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    picture = browser.find_element(By.ID, "treasure")
    value_x = picture.get_attribute("valuex")
    x = calc(value_x)

    input = browser.find_element(By.ID, "answer").send_keys(x)
    for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
        browser.find_element(By.CSS_SELECTOR, selector).click()

finally:
    time.sleep(10)
    browser.quit()
