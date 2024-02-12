import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/v1/")
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)
    request.cls.driver = driver
    request.cls.wait = wait
    yield driver
    driver.quit()