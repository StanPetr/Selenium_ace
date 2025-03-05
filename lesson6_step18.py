from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 


try: 
    
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    
    browser.get("http://suninjuly.github.io/wait1.html")

    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    
    
    
    
    # link = "http://suninjuly.github.io/redirect_accept.html"
    # driver = webdriver.Chrome()
    # driver.get(link)

    # sbm_button = driver.find_element(By.CLASS_NAME, "trollface")
    # sbm_button.click()
    
    # new_window = driver.window_handles[1]
    # driver.switch_to.window(new_window)
    
    # def calc(x):
          # return str(math.log(abs(12*math.sin(int(x_text)))))

    # x = driver.find_element(By.CSS_SELECTOR, "#input_value")
    # x_text = x.text
    # print (x_text)
    # y = calc(x)
    
    # input_link = driver.find_element(By.ID, "answer")
    # input_link.send_keys(y)
    
    # sbm_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
    # sbm_button.click()
    
    
    # confirm = driver.switch_to.alert
    # confirm.accept()
    
    # def calc(x):
          # return str(math.log(abs(12*math.sin(int(x_text)))))

    # x = driver.find_element(By.CSS_SELECTOR, "#input_value")
    # x_text = x.text
    # print (x_text)
    # y = calc(x)
    
    # input_link = driver.find_element(By.ID, "answer")
    # input_link.send_keys(y)
    
    # sbm_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
    # sbm_button.click()



    # input_name = driver.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    # input_name.send_keys("Ivan")

    # input_surname = driver.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    # input_surname.send_keys("Ivanov")
    
    # input_email = driver.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    # input_email.send_keys("1231@email.com")

    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    # element = driver.find_element(By.ID, 'file')
    # element.send_keys(file_path)
    
     
    
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
    
    # checkbox = driver.find_element(By.ID, "robotCheckbox")
    # checkbox.click() 
    
    # raddiobutton = driver.find_element(By.ID, "robotsRule")
    # driver.execute_script("return arguments[0].scrollIntoView(true);", raddiobutton)
    # raddiobutton.click() 
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
