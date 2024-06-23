import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    print("Creating Chrome driver")
    my_driver = webdriver.Chrome()

    my_driver.implicitly_wait(10)
    yield my_driver
    print("Closing Chrome driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (only chrome supported)"
    )
