from selenium.webdriver.common.by import By

class LogInPageLocators(object):
    LOG_IN_BUTTON = (By.ID, "login-button")
    USERNAME_TEXTBOX = (By.ID, "user-name")
    PASSWORD_TEXTBOX = (By.ID, "password")
