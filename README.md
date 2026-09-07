# OrangeHRM Automation Framework

A Selenium + Pytest based test automation framework for testing the OrangeHRM web application.

This project demonstrates practical QA automation concepts including Page Object Model (POM), reusable fixtures, explicit waits, parameterized testing, and automated test execution.

## 🚀 Project Overview

The framework automates important OrangeHRM functionality such as:

- Valid login
- Invalid login validation
- Navigation to the PIM module
- Adding a new employee
- Searching for an employee
- Employee record validation

The framework is designed using the **Page Object Model (POM)** to keep test cases clean, maintainable, and reusable.

## 🛠️ Technologies Used

- Python
- Selenium WebDriver
- Pytest
- Chrome WebDriver
- Page Object Model (POM)
- Git & GitHub

## 📁 Project Structure

```text
OrangeHRM-Automation-Framework/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── pim_page.py
│   └── add_employee_page.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_pim.py
│   ├── test_add_employee.py
│   ├── test_search_employee.py
│   └── test_employee_exists.py
│
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
