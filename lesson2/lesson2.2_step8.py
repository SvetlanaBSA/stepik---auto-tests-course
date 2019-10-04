from selenium import webdriver
import time
import os

try: 

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("[name=firstname]")
    first_name.send_keys("Sv")
    last_name = browser.find_element_by_css_selector("[name=lastname]")
    last_name.send_keys("Ber")
    email = browser.find_element_by_css_selector("[name=email]")
    email.send_keys("email@test.com")
    choose_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'svfile.txt')
    choose_file.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

