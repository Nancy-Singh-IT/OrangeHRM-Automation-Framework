from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_navigate_to_pim(driver):

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    pim_page = PIMPage(driver)

    pim_page.click_pim()

    assert "/pim/viewEmployeeList" in driver.current_url