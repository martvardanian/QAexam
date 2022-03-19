import unittest
import time

from selenium.webdriver.common.by import By

from Configs.google_browser import ChromeBrowser
from Locators.hotels_page_locators import HotelsLocators
from Pages.login_page import LoginPage
from Pages.search_book_page import SearchHotelAndBook


class SearchHotelYerevanAndBook(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.phptravels.net/"

    def test_search_and_book(self):
        driver = ChromeBrowser.driver
        ChromeBrowser.driver.get(self.url)
        login_page = LoginPage(driver)
        login_page.login()

        search_book = SearchHotelAndBook(driver)
        search_book.search_book()

        assert ChromeBrowser.driver.find_element(By.XPATH, HotelsLocators.credit_card)  == "Card holder name *"


    def tearDown(self):
        ChromeBrowser.driver.quit()


if __name__ == "__main__":
    unittest.main()