import unittest
from time import time

from selenium.webdriver.common.by import By

from Configs.google_browser import ChromeBrowser
from Pages.login_page import LoginPage
from Pages.sign_up_page import SignUpPage


class LoginAccount(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.phptravels.net/"

    def test_login(self):
        driver = ChromeBrowser.driver
        ChromeBrowser.driver.get(self.url)
        login_page = LoginPage(driver)
        login_page.login()
        assert ChromeBrowser.driver.current_url == "https://www.phptravels.net/account/dashboard"

    def tearDown(self):
        ChromeBrowser.driver.quit()


if __name__ == "__main__":
    unittest.main()