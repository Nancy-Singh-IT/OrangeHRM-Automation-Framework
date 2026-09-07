from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    dashboard_heading = (
        By.CSS_SELECTOR,
        "h6.oxd-topbar-header-breadcrumb-module"
    )

    time_at_work = (
        By.XPATH,
        "//p[normalize-space()='Time at Work']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_dashboard_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.dashboard_heading)
        )
        return heading.is_displayed()

    def is_time_at_work_displayed(self):
        widget = self.wait.until(
            EC.visibility_of_element_located(self.time_at_work)
        )
        return widget.is_displayed()