import unittest
from selenium import webdriver
from Pages import page


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\grale\Desktop\Projects\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.saucedemo.com/")

    def test_title(self):
        loginPage = page.LogInPage()
        assert loginPage.is_title_matches()

    def tearDown(self):
        self.driver.close()
