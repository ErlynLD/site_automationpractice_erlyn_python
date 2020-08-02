import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # ChromeDriver instance
    browser = selenium.webdriver.Chrome()

    # Setting implicitly wait of ChromeDriver
    browser.implicitly_wait(10)

    # Return WebDriver instance
    yield browser

    # Quit WebDriver
    browser.quit()
