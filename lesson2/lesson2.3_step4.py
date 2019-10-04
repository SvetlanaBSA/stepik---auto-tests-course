from selenium import webdriver
import time
import math

try: 

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("[type=submit]")
    first_name.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    # Ввод ответа в поле
    input1 = browser.find_element_by_id("answer") 
    input1.send_keys(y)
    
    button =  browser.find_element_by_tag_name("button") 
    button.click()


    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()