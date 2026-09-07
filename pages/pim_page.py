from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.pim_menu = (
            By.XPATH,
            "//a[contains(@href, '/pim/viewPimModule')]"
        )

        self.add_button = (
            By.XPATH,
            "//button[normalize-space()='Add']"
        )

        self.employee_list_heading = (
            By.XPATH,
            "//h5[normalize-space()='Employee Information']"
        )

        self.employee_name_search = (
            By.XPATH,
            "//label[normalize-space()='Employee Name']"
            "/following::input[@placeholder='Type for hints...'][1]"
        )

        self.autocomplete_option = (
            By.XPATH,
            "//div[@role='listbox']"
            "//div[contains(@class,'oxd-autocomplete-option')]"
        )

        self.employee_rows = (
            By.XPATH,
            "//div[@role='row']"
        )

    def click_pim(self):
        pim = self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        )
        pim.click()

        self.wait.until(
            EC.url_contains("/pim/viewEmployeeList")
        )

    def click_add(self):
        add = self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        )
        add.click()

    def wait_for_employee_list(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.employee_list_heading
            )
        )
    def is_employee_displayed(self, employee_name):

        rows = self.driver.find_elements(
            By.XPATH,
            "//div[@role='row']"
        )
        for row in rows:
            if employee_name.lower() in row.text.lower():
                return True

        return False

    def search_employee(self, employee_name):

        # Open the employee search/filter section
        filter_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//h5[normalize-space()='Employee Information']/following::button[1]"
                )
            )
        )
        filter_button.click()

        # Enter employee name
        search_field = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//label[normalize-space()='Employee Name']/following::input[@placeholder='Type for hints...'][1]"
                )
            )
        )

        search_field.click()
        search_field.send_keys(employee_name)

        # Select autocomplete suggestion
        suggestion = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@role='listbox']//div[contains(@class,'oxd-autocomplete-option')]"
                )
            )
        )

        suggestion.click()

        # Click Search button
        search_button = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Search']"
                )
            )
        )

        search_button.click()

        # Wait for results table
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@role='row']")
            )
        )