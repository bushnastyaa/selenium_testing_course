from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://SunInJuly.github.io/execute_script.html")
    browser.execute_script("window.scrollBy(0, 150);")

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer").send_keys(y)
    for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-primary']:
        browser.find_element(By.CSS_SELECTOR, selector).click()

finally:
    time.sleep(10)
    browser.quit()
