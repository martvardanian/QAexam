from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Locators.hotels_page_locators import HotelsLocators
from Locators.signup_locators import SignUpLocators
from selenium.webdriver.support import expected_conditions as EC
import time


class SignUpPage:
    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        self.driver.find_elements(By.XPATH, SignUpLocators.signup_button_xpath)[0].click(),
        self.driver.find_elements(By.XPATH, SignUpLocators.first_name_input_xpath)[0].send_keys('Mart'),
        self.driver.find_elements(By.XPATH, SignUpLocators.last_name_input_xpath)[0].send_keys('Vardanian'),
        self.driver.find_elements(By.XPATH, SignUpLocators.phone_number_input_xpath)[0].send_keys('37441111111'),
        self.driver.find_elements(By.XPATH, SignUpLocators.email_input_xpath)[0].send_keys('vardanian@gmail.com'),
        self.driver.find_elements(By.XPATH, SignUpLocators.password_input_xpath)[0].send_keys('111111'),
        time.sleep(3)

        # self.driver.find_elements(By.XPATH, SignUpLocators.signup_next_button_xpath)[0].click(),
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, SignUpLocators.signup_next_button_xpath))).click()
