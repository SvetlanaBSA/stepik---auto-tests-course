import pytest
import time
import math
from selenium import webdriver


@pytest.fixture
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
    y = str(math.log(int(time.time())))

    time.sleep(5)
    answer_field = browser.find_element_by_class_name("textarea")
    answer_field.send_keys(y)

    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()
    time.sleep(5)

    message = browser.find_element_by_class_name("smart-hints__hint")
    assert message.text == "Correct!", f"{message} "



