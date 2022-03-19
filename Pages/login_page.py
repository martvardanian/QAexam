from selenium.webdriver.common.by import By

from Locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.find_elements(By.XPATH, LoginLocators.login_button_xpath)[0].click(),
        self.driver.find_elements(By.XPATH, LoginLocators.email_input_xpath)[0].send_keys('vardanian@gmail.com'),
        self.driver.find_elements(By.XPATH, LoginLocators.password_input_xpath)[0].send_keys('111111'),
        self.driver.find_elements(By.XPATH, LoginLocators.login_next_button_xpath)[0].click()
