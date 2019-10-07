import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_answers_link(browser, page_link):
    link = f"https://stepik.org/lesson/{page_link}/step/1"
    browser.get(link)

    answer_field = browser.find_element_by_id("ember1530")
    answer = math.log(int(time.time()))
    answer_field.send_keys(answer)

    button_submit = browser.find_element_by_class_name("submit-submission")
    button_submit.click()

    time.sleep(15)


