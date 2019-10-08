import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: es or fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    browser_name = request.config.getoption("--browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if user_language == "es" or user_language == "fr":
        link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("--language should be fr or es")
    #browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()

