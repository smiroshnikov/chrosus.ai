import time
from threading import Thread

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ExCon
from selenium.webdriver.support.wait import WebDriverWait

# constants


MAC_PATH = "/Users/smiroshn/work/chromedriver/chromedriver"
WIN_PATH = "H:\Webdrivers\chromedriver_win32\chromedriver.exe"
CREEDENTIALS = ["automation@gmail.com", "rhrDBWT78iwU"]
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
        search_box = self.driver.find_element_by_xpath("//input[@name='search']")
        # search_box = self.driver.find_element_by_xpath(
        #     "//div/form/input")
        # search_box clicking creates a selenium exception , so in order to queue action chains
        # actions = ActionChains(self.driver)

        AS57 = WebDriverWait(self.driver, 10).until(
            ExCon.element_to_be_clickable((By.XPATH, "//div/h4[contains(string(), ' 57 - Automation Standup')]")))
        # i can get a list of those , and go for last one . not during home-task
        AS57.click()
        self.actions.move_to_element(search_box)
        self.actions.click()
        self.actions.perform()
        search_box.send_keys(search_string)
        search_box.send_keys(Keys.RETURN)

    def get_transcript_search_results(self):
        search_result_list = self.driver.find_elements(By.XPATH("//div/span[contains(@class,'text')]"))

    def parse_transcript_search_results(self, result_list):
        top_search_results = 0
        bottom_search_results = 0
        web_to_string = []
        for e in result_list:
            web_to_string.append(e.text)
        # for text_e in web_to_string:
        #     print(text_e)
        # current = ([int(s) for s in web_to_string[0].split() if s.isdigit()])[0]
        print(top_search_results + "CURRENT!")
        # other = ([int(s) for s in web_to_string[0].split() if s.isdigit()])[1]
        #
        # print(bottom_search_results + "bottom")
        #
        # print(f"top {current + other}")


def assert_search_results(self):
    search_string = self.driver.find_element_by_xpath(
        "//span[contains(@class, 'text overflow-ellipsis spring')]").text
    search_results = {"current_meeting": ([int(s) for s in search_string.split() if s.isdigit()])[0],
                      "other_meetings ": ([int(s) for s in search_string.split() if s.isdigit()])[1]}

    page_results = 6

    assert (search_results["current_meeting"] + search_results[
        "other_meetings"]) == page_results, "invalid number of results!"


if __name__ == "__main__":
    chorus = ChorusHW(DRIVER, ACTIONS)
    chorus.navigate_to_login_page()
    chorus.login_into_chorus(CREEDENTIALS, USER_ACC_URL)
    chorus.implicit_wait(5)
    chorus.click_on_account(ACCOUNT_NAME)
    chorus.search_transcripts("bob")
    RES = DRIVER.find_elements(By.XPATH, "//div/span[contains(@class,'text')]")
    for item in RES:
        print(item.text)
    # chorus.parse_transcript_search_results(RES)

    # chorus.get_transcript_search_results()
    # chorus.assert_search_results()

    # chorus.quit()

    # //div/div/div[contains(string(), "Matches in other")] crappy path but its working

    # generally , this would be separated into few  classes , i would separate instantiation,
    # initialization , and utility classes separately
