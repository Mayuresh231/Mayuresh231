from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.BaseTest import BaseTest


class TestClass(BaseTest):
    # class variables
    username_locator = (By.XPATH, "//input[@id = 'user-name'] ")
    password_locator = (By.XPATH, "// input[@name ='password']")
    lgn_btn_locator = (By.ID, "login-button")

    def test_login_with_valid_credentials(self):
        self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys("standard_user")
        self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(self.lgn_btn_locator)).click()

    def test_login_with_locked_out_user(self):
        self.wait.until(EC.presence_of_element_located(self.username_locator)).send_keys("locked_out_user")
        self.wait.until(EC.presence_of_element_located(self.password_locator)).send_keys("secret_sauce")
        self.wait.until(EC.element_to_be_clickable(self.lgn_btn_locator)).click()
