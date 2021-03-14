from Locators.locator import *
from Elements.element import LogInPageElement

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LogInPage(BasePage):
    def is_title_matches(self):
        return "Swag Labs" in self.driver.title

    def click_log_in(self):
        element = self.driver.find_element(*LogInPageLocators.LOG_IN_BUTTON)
        element.click()
