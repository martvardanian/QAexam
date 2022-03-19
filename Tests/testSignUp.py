import unittest
from time import time

from selenium.webdriver.common.by import By

from Configs.google_browser import ChromeBrowser
from Pages.login_page import LoginPage
from Pages.sign_up_page import SignUpPage


class SignUpAccount(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.phptravels.net/"

    def test_sign_up(self):
        driver = ChromeBrowser.driver
        ChromeBrowser.driver.get(self.url)
        sign_up_page = SignUpPage(driver)
        sign_up_page.sign_up()

        assert ChromeBrowser.driver.current_url == "https://www.phptravels.net/login/signup"

    def tearDown(self):
        ChromeBrowser.driver.quit()


if __name__ == "__main__":
    unittest.main()