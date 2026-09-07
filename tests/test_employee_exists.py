from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_employee_exists(driver):

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    pim_page = PIMPage(driver)
    pim_page.click_pim()

    pim_page.wait_for_employee_list()

    pim_page.go_to_page(2)

    assert pim_page.verify_employee("Nancy Singh", "0424")