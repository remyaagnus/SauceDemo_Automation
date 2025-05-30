from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException


class MainPage:
    LOGO_LOCATOR = (By.XPATH, '//div[@class="app_logo"]')

    def __init__(self, driver):
        self.driver = driver

    def verify_logo(self):

        try:
            logo = self.driver.find_element(*self.LOGO_LOCATOR)

            if logo.is_displayed():
                print("Login successful: logo found.")
                return True
            else:
                print("Login failed: logo not displayed.")
                return False
        except NoSuchElementException:
            print("Login failed: logo element not found.")
            return False

