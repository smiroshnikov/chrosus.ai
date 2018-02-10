from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# constants
from selenium.webdriver.support import wait, ui
from selenium.webdriver.support.wait import WebDriverWait

MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
WIN_PATH = "H:\Webdrivers\chromedriver_win32\chromedriver.exe"
CREEDENTIALS = ["automation@gmail.com", "rhrDBWT78iwU"]
USER_ACC_URL = "https://chorus.ai/blueprint/205426"
DRIVER = webdriver.WebDriver(WIN_PATH)
ACCOUNT_NAME = "Automation.com"


class ChorusHW:

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.chorus.ai/login'

    def navigate_to_login_page(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def login_into_chorus(self, credentials, user_acc_url):
        # email_box = "//div[contains(@class, 'email-field')]"
        email_box = "//input[@name='email']"
        email_box_element = self.driver.find_element_by_xpath(email_box)
        email_box_element.click()
        email_box_element.clear()  # just in case
        email_box_element.send_keys(credentials[0])
        email_box_element.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)  # not too elegant
        password_box = "//input[@name='password']"
        password_box_element = self.driver.find_element_by_xpath(password_box)
        password_box_element.click()
        password_box_element.send_keys(credentials[1])
        password_box_element.send_keys(Keys.RETURN)
        # self.driver.get(user_acc_url) # redirect is broken  :(

    def implicit_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def click_on_account(self, account_name):
        # self.driver.find_element_by_partial_link_text(account_name).click()
        self.driver.find_element_by_xpath("//*[contains(text(),'Automation.com')]").click()
        # self.driver.find_element_by_xpath("//*[contains(text(),"+account_name+"')]").click()

    def click_hide_under_10_calls(self):
        chorus_checkbox = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//div[contains(@class,'chorus-checkbox')]"))
        chorus_checkbox.click()


if __name__ == "__main__":
    chorus = ChorusHW(DRIVER)
    chorus.navigate_to_login_page()
    chorus.login_into_chorus(CREEDENTIALS, USER_ACC_URL)
    chorus.implicit_wait(5)
    chorus.click_on_account(ACCOUNT_NAME)
    chorus.implicit_wait(5)
    chorus.click_hide_under_10_calls()

    # chorus.quit()
