
from selenium.webdriver.common.by import By

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_btn = (By.LINK_TEXT, "Add Employee")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_menu = (By.LINK_TEXT, "Employee List")

    def add_employee(self, first_name, last_name):
        self.driver.find_element(*self.add_employee_btn).click()
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.save_button).click()

    def go_to_employee_list(self):
        self.driver.find_element(*self.employee_list_menu).click()
