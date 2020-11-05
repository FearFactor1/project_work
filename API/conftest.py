import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url_api",
        default="https://reqres.in/",
        help="This is request url"
    )


@pytest.fixture
def url_api(request):
    return request.config.getoption("--url_api")