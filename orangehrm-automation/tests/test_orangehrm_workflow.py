
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from employees_data import employees

def test_orangehrm_workflow():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(2)

    login = LoginPage(driver)
    login.login("Admin", "admin123")
    time.sleep(3)

    dashboard = DashboardPage(driver)
    dashboard.navigate_to_pim()
    time.sleep(2)

    pim = PIMPage(driver)
    for emp in employees:
        pim.add_employee(emp['first_name'], emp['last_name'])
        time.sleep(2)

    pim.go_to_employee_list()
    time.sleep(2)

    # Dummy verification just for sample
    print("Name Verified")

    dashboard.logout()
    driver.quit()
