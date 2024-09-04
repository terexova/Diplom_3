import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()

    yield chrome_driver

    chrome_driver.quit()
