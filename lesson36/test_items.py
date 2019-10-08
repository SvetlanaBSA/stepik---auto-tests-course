import time
import pytest


class TestSuite():

    def test_add_button_exist(self, browser, language):
        language = language
        if language == "es" or language == "fr":
            link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        else:
            raise pytest.UsageError("--language should be fr or es")
        browser.get(link)
        time.sleep(5)
        button_add_to_basket = browser.find_element_by_class_name("btn-add-to-basket")
        assert button_add_to_basket.is_element_present, "Button is NOT exist"

