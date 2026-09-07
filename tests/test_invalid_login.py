import pytest

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "wrongpassword"),
        ("wronguser", "admin123"),
        ("wronguser", "wrongpassword"),
    ]
)
def test_invalid_login(driver, username, password):

    login_page = LoginPage(driver)

    login_page.login(username, password)

    error_message = login_page.get_invalid_credentials_message()

    assert error_message == "Invalid credentials"