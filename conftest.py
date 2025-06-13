# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    
    service = webdriver.chrome.service.Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
