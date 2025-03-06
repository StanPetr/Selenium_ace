import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAbs(unittest.TestCase):
    
    def test_registration_page(self):
        
        browser = webdriver.Chrome() 
        link1 = "http://suninjuly.github.io/registration1.html"
        browser.get(link1)    
        
        # заполняем обязательные поля
        f_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        f_name_field.send_keys("Ivan")
                
        l_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        l_name_field.send_keys("Petrov")
                
        email_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_field.send_keys("email@email.ru")
        
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome texts are differ")
        
        
       
        
    def test_registration_page(self):
        
        browser = webdriver.Chrome() 
        link1 = "http://suninjuly.github.io/registration2.html"
        browser.get(link1)    
        
        # заполняем обязательные поля
        f_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        f_name_field.send_keys("Ivan")
                
        l_name_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        l_name_field.send_keys("Petrov")
                
        email_field = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_field.send_keys("email@email.ru")
        
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Welcome texts are differ")
        
        
if __name__ == "__main__":
    unittest.main()