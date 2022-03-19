import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Locators.hotels_page_locators import HotelsLocators
from selenium.webdriver.support import expected_conditions as EC

class SearchHotelAndBook:
    def __init__(self, driver):
        self.driver = driver

    def search_book(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, HotelsLocators.hotel_button_xpath).click(),
        time.sleep(2)
        self.driver.find_element(By.XPATH, HotelsLocators.search_input_xpath).click(),
        self.driver.find_element(By.XPATH, HotelsLocators.write_in_input_xpath).send_keys('Yerevan')
        time.sleep(2)
        self.driver.find_element(By.XPATH, HotelsLocators.yerevan_click_xpath).click(),
        self.driver.find_element(By.XPATH, HotelsLocators.search_button_xpath).click(),
        time.sleep(1)
        self.driver.find_element(By.XPATH, HotelsLocators.details_xpath).click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.search_button))).click()
        time.sleep(3)
        list_hotels = self.driver.find_elements(By.XPATH, HotelsLocators.sel_r)
        list_hotels[1].click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(2)

        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, HotelsLocators.body))).send_keys(Keys.ARROW_DOWN)

        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.book_now))).click()
        time.sleep(7)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.name_input_xpath))).send_keys("Mart Vradnayn")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.email_input))).send_keys("mart@mart.com")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.retype_email_input))).send_keys("mart@mart.com")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.phone_number_input))).send_keys("22222222")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, HotelsLocators.next_final_button))).click()

        time.sleep(5)






