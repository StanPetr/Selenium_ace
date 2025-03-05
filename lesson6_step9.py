from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    driver = webdriver.Chrome()
    driver.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
  
    x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    people_radio = driver.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    robots_radio = driver.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    
    input_link = driver.find_element(By.CSS_SELECTOR, "#answer")
    input_link.send_keys(y)
    
    checkbox = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click() 
    
    raddiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
    raddiobutton.click() 
    
    sbm_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    sbm_button.click() 
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()