from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_search_employee(driver):

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    pim_page = PIMPage(driver)
    pim_page.click_pim()

    pim_page.wait_for_employee_list()

    pim_page.search_employee("Nancy")

    assert pim_page.is_employee_displayed("Nancy")

