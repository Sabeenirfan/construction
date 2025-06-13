import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # ❌ Remove this line
    # options.add_argument("--user-data-dir=/tmp/chrome-user-data")

    service = Service('/usr/bin/chromedriver')  # Ensure this is the correct path in your container
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
