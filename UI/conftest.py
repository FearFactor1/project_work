import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://gmail.com",
                     help="choose your browser")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.headless = False
        chrome_options.add_argument('start-fullscreen')
        wd = webdriver.Chrome(options=chrome_options, executable_path="chromedriver.exe")
#        wd = webdriver.Remote(command_executor="http://selenium__standalone-chrome:4444/wd/hub", options=chrome_options)
    elif browser == "firefox":
        firefox_option = FirefoxOptions()
        wd = webdriver.Firefox(options=firefox_option)
        wd.maximize_window()
    else:
        raise Exception(f"{request.param} is not supported!")

    request.addfinalizer(wd.quit)
    return wd