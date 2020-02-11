import time


def test_add_button_exist(browser):
    time.sleep(30)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0, "Button is NOT exist"
