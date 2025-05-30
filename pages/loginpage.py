from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    USERNAME_LOCATOR = (By.ID, 'user-name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BTN_LOCATION= (By.ID, 'login-button')

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(*self.USERNAME_LOCATOR).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_LOCATOR).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN_LOCATION).click()

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
