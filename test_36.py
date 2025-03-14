from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nQuit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_something(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    
    # Ждем пока не появится кнопка реги и нажимаем кнопку реги
    button1 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
    )
    button1.click()
    
    # Вводим логин и пароль
    input1 = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    input1.send_keys("///")
    input2 = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    input2.send_keys("///")
    
    # Отправляем заполненную форму
    button2 = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn"))
    )
    button2.click()
    
    try:# Кнопка "Решить снова" активна
        button3 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        button3.click()
        print('Кнопка "Решить снова" активна, поле textarea неактивно')
        
    except TimeoutException:# Кнопки "Решить снова" нет
        print('Кнопка "Решить снова" не обнаружена, поле textarea активное')
        
    finally:
        # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
        # при этом не используем time.sleep!
        WebDriverWait(browser, 10).until_not(
        EC.element_attribute_to_include((By.CSS_SELECTOR, "textarea.ember-text-area"), 'disabled')
        )
        answer = math.log(int(time.time()))
        input_answer = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        input_answer.send_keys(answer)
        
        # Нажимаем кнопку "Отправить"
        button4 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button4.click()
        
        # Ждем пока не появится фидбек, что ответ верный
        feedback = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        
        #Сравниваем, что фидбек полностью совпадает с "Correct!"
        assert feedback.text == "Correct!", f"{feedback.text}"
