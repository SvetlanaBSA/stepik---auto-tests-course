import time


def test_add_button_exist(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    time.sleep(5)
    button_add_to_basket = browser.find_element_by_class_name("btn-add-to-basket")
    assert button_add_to_basket.is_element_present, "Button is NOT exist"

