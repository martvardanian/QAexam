from selenium import webdriver


class ChromeBrowser:
    driver = webdriver.Chrome(executable_path='/home/erida-employee/Desktop/Mart/Driver/chromedriver')
    driver.maximize_window()