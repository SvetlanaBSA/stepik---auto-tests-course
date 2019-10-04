from selenium import webdriver
import time
import math

try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
	# Скрол до поля ввода ответа
    input1 = browser.find_element_by_id("answer") 
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1) 
    # Ввод ответа в поле
    input1.send_keys(y)
    # Выбор нужных чек-боксов
    option1 = browser.find_element_by_id("robotCheckbox") 
    option1.click()
    option2 = browser.find_element_by_id("robotsRule") 
    option2.click()
    # Скрол страницы до кнопки Submit
    button =  browser.find_element_by_tag_name("button") 
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # Отправляем заполненную форму
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

