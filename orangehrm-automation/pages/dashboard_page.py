
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.logout_menu = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def navigate_to_pim(self):
        self.driver.find_element(*self.pim_menu).click()

    def logout(self):
        self.driver.find_element(*self.logout_menu).click()
        self.driver.find_element(*self.logout_button).click()
