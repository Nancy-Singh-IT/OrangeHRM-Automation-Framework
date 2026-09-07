from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))

    dashboard_page = DashboardPage(driver)

    assert dashboard_page.is_dashboard_displayed()
    assert dashboard_page.is_time_at_work_displayed()