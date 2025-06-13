import pytest
import tempfile
import uuid
from selenium import webdriver

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    
    # Essential Docker/Jenkins options
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # Create unique user data directory - THIS IS THE KEY FIX
    unique_id = str(uuid.uuid4())
    temp_dir = f"/tmp/chrome-user-data-{unique_id}"
    options.add_argument(f"--user-data-dir={temp_dir}")
    
    # Additional stability options
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-debugging-port=0")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Your existing test functions go here...
