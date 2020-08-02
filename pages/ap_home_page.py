from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Home:
    # This tuple becomes a By in usage
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

    def __init__(self, browser):
        self.browser = browser

    def click_on_sign_in_link(self):
        # Here we are passing multiple positional arguments thanks to Python feature *
        self.browser.find_element(*self.SIGN_IN_LINK).click()
        WebDriverWait(self.browser, 10)\
            .until(expected_conditions.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'Authentication')]")))
        self.browser.save_screenshot("screenshots\\result.png")
        return self.browser.title
