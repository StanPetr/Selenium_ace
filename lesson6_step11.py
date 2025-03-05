from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    z = str(int(x)+int(y))
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    choose_answer = select.select_by_value(value = z)
    
    sbm_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    sbm_button.click() 
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()