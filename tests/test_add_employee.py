
from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage


def test_add_employee(driver):

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    pim_page = PIMPage(driver)
    pim_page.click_pim()
    pim_page.click_add()

    add_employee_page = AddEmployeePage(driver)

    add_employee_page.enter_first_name("Nancy")
    add_employee_page.enter_middle_name("QA")
    add_employee_page.enter_last_name("Tester")

    add_employee_page.click_save()

