from selenium.webdriver.common.by import By


class APLoginPage:

    EMAIL = (By.ID, "email")
    PASSWORD = (By.NAME, "passwd")

    def __int__(self, email, password):
        self.email = email,
        self.password = password

