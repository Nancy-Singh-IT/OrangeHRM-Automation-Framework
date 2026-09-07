from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # Locators
    username_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_button = (By.CLASS_NAME, "orangehrm-login-button")

    invalid_credentials_message = (
        By.XPATH,
        "//*[normalize-space()='Invalid credentials']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_invalid_credentials_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(
                self.invalid_credentials_message
            )
        )
        return message.text