from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddEmployeePage:

    first_name = (
        By.NAME,
        "firstName"
    )

    middle_name = (
        By.NAME,
        "middleName"
    )

    last_name = (
        By.NAME,
        "lastName"
    )

    save_button = (
        By.XPATH,
        "//button[normalize-space()='Save']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name):
        field = self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        )
        field.send_keys(first_name)

    def enter_middle_name(self, middle_name):
        field = self.wait.until(
            EC.visibility_of_element_located(self.middle_name)
        )
        field.send_keys(middle_name)

    def enter_last_name(self, last_name):
        field = self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        )
        field.send_keys(last_name)

    def click_save(self):
        save = self.wait.until(
            EC.element_to_be_clickable(self.save_button)
        )
        save.click()