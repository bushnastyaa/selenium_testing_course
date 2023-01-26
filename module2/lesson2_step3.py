from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    result = str(int(x)+int(y))

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(result)
    button = browser.find_element(By.CLASS_NAME, "btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
