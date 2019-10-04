import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	
	browser = webdriver.Chrome()
	# говорим WebDriver ждать все элементы в течение 5 секунд
	browser.implicitly_wait(5)

	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	
	price = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100")
	)
	button = browser.find_element(By.ID, "book")
	button.click()
	
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	# Ввод ответа в поле
	input1 = browser.find_element_by_id("answer") 
	input1.send_keys(y)
	
	button =  browser.find_element_by_id("solve") 
	button.click()
	
		
finally:
	time.sleep(12)
	browser.quit()