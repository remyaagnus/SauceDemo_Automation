import time
from scripts import data
from pom.loginpage import LoginPage
from scripts import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class TestSauceDemo:

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        # Check if the Urban Routes URL is reachable before running tests
        if helpers.is_url_reachable(data.SAUCEDEMO_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_login(self):
        self.driver.get(data.SAUCEDEMO_URL)
        page = LoginPage(self.driver)

        page.login(data.USERNAME,data.PASSWORD)

        time.sleep(10)
