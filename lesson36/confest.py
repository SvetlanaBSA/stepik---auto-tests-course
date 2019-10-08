import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption1("--browser_name")
    browser = None
    language = request.config.getoption2("--language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if language == "es" or language == "fr":
        link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    else:
        raise pytest.UsageError("--language should be fr or es")
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()

