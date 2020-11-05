import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://gmail.com",
                     help="choose your browser")
    parser.addoption("--executor", default="10.20.30.57")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser}
    )
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver