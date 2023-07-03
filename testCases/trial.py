import string
import random
import pytest

from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomerPage

from selenium import webdriver
import time
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomerPage

class Test_seacrh_customer_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_seacrhBy_email(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)
        self.logger.info("1")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("2")

        # AddCustomer

        self.logger.info("1")
        self.Add_cust = AddCustomerPage(self.driver)
        self.logger.info("2")

        self.Add_cust.ClickOnCustomerMenu()
        self.logger.info("3")

        self.Add_cust.ClickOnSubCustomerMenu()
        self.logger.info("4")

        Search_cust=SearchCustomerPage(self.driver)
        Search_cust.SetEmail("victoria_victoria@nopCommerce.com")
        Search_cust.Clicksearch()
        status=Search_cust.searchByEmail("victoria_victoria@nopCommerce.com")

        assert True==status
