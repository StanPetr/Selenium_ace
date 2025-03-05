from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/huge_form.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("питон")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

    # не забываем оставить пустую строку в конце файла