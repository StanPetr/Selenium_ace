from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
          return str(math.log(abs(12*math.sin(int(x_text)))))

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x_text = x.text
    print (x_text)
    y = calc(x)
    
    input_link = browser.find_element(By.ID, "answer")
    input_link.send_keys(y)
    
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click() 
    
    raddiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", raddiobutton)
    raddiobutton.click() 
    
    sbm_button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", sbm_button)
    sbm_button.click() 
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
