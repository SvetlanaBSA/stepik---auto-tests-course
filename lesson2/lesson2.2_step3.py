from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select 

try: 

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x1 = x_element.text
    x_element2 = browser.find_element_by_id("num2")
    x2 = x_element2.text
    y = str(int(x1) + int(x2))
   	
    select = Select(browser.find_element_by_id("dropdown")) 
    select.select_by_value(y) # ищем элемент с текстом "Python
    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

