import time

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ex_con
from selenium.webdriver.support.wait import WebDriverWait
import logging

# constants/globals
MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
WIN_PATH = "H:\Webdrivers\chromedriver_win32\chromedriver.exe"
CREDENTIALS = ["automation@gmail.com", "rhrDBWT78iwU"]
USER_ACC_URL = "https://chorus.ai/blueprint/205426"
DRIVER = webdriver.WebDriver(WIN_PATH)
ACTIONS = ActionChains(DRIVER)
ACCOUNT_NAME = "Automation.com"


class ChorusHW:

    def __init__(self, driver, actions):
        self.driver = driver
        self.url = 'https://www.chorus.ai/login'
        self.actions = actions

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
        # self.driver.find_element_by_xpath("//*[contains(text(),"+account_name+"')]").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'Automation.com')]").click()

    def click_hide_under_10_calls(self):
        chorus_checkbox = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//div[contains(@class,'chorus-checkbox')]"))
        chorus_checkbox.click()

    def search_transcripts(self, search_string):
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath("//input[@name='search']")
        # search_box = self.driver.find_element_by_xpath(
        #     "//div/form/input")
        # search_box clicking creates a selenium exception , so in order to queue action chains
        # actions = ActionChains(self.driver)

        AS57 = WebDriverWait(self.driver, 10).until(
            ex_con.element_to_be_clickable((By.XPATH, "//div/h4[contains(string(), ' 57 - Automation Standup')]")))
        # i can get a list of those , and go for last one . not during home-task
        AS57.click()
        self.actions.move_to_element(search_box)
        self.actions.click()
        self.actions.perform()
        search_box.send_keys(search_string)
        search_box.send_keys(Keys.RETURN)

    def validate_transcript_search_results_test(self):

        """
        Extracts all search results to an element list
        Converts web elements to text list
        extracts numeric values from test list
        validates that search results on the top are equal to total number of results at the bottom
        """

        web_element_list = self.driver.find_elements_by_xpath("//div/span[contains(@class,'text')]")
        bottom_summary = 0
        sr = []
        for item in web_element_list:
            sr.append(item.text)

        # sr = [
        #     '"bob" - 0 Matches in this meeting , 7 Matches in other meetings',
        #     '1 Matches found in "1 - Call"',
        #     '1 Matches found in "7 - Automation Standup"',
        #     '1 Matches found in "35 - Automation Standup"',
        #     '3 Matches found in "46 - Automation Standup"']

        if len(sr) > 0:
            top_summary = ([int(s) for s in sr[0].split() if s.isdigit()])[0] + \
                          ([int(s) for s in sr[0].split() if s.isdigit()])[1]
            print(top_summary)

            for i in range(1, len(sr)):
                bottom_summary += ([int(s) for s in sr[i].split() if s.isdigit()])[0]
            print(bottom_summary)
            try:
                assert top_summary == bottom_summary, "invalid number of search results"
                passed = True
            except AssertionError as e:
                print(e)
                passed = False
        return passed


if __name__ == "__main__":
    chorus = ChorusHW(DRIVER, ACTIONS)
    chorus.navigate_to_login_page()
    chorus.login_into_chorus(CREDENTIALS, USER_ACC_URL)
    chorus.click_on_account(ACCOUNT_NAME)
    time.sleep(3)  # no i don't do those in real life , wasn't able to figure out what element is loaded last
    chorus.search_transcripts("bob")
    chorus.validate_transcript_search_results_test()
    chorus.quit()

    # //div/div/div[contains(string(), "Matches in other")] crappy path but its working

    # generally , this would be separated into few  classes , i would separate instantiation,
    # initialization , and utility classes separately
