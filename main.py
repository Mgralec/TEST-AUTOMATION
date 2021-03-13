import unittest
from selenium import webdriver
from Pages import page

class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Users\grale\Desktop\Projects\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.saucedemo.com/")
    def tearDown(self):
        self.driver.close()