from scripts import data
from pages.loginpage import LoginPage
from scripts import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages.mainpage import MainPage


class TestSauceDemo:

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        options = webdriver.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False  # <-- Disable leak detection
        }
        options.add_experimental_option("prefs", prefs)

        cls.driver = webdriver.Chrome(options=options)

        # Check if the Urban Routes URL is reachable before running tests
        if helpers.is_url_reachable(data.SAUCEDEMO_URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_login(self):
        self.driver.get(data.SAUCEDEMO_URL)
        page = LoginPage(self.driver)
        mainpage = MainPage(self.driver)

        page.login(data.USERNAME, data.PASSWORD)

        assert mainpage.verify_logo() is True

    def test_invalid_login(self):
        self.driver.get(data.SAUCEDEMO_URL)
        page = LoginPage(self.driver)
        mainpage = MainPage(self.driver)

        page.login("wronguser", data.PASSWORD)

        assert mainpage.verify_logo() is False
