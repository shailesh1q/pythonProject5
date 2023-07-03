import pytest
import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomerPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomerPage


class Test_seacrh_customer_004:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("test_003")
        self.driver = setup
        self.driver.get(self.baseUrl)

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("login succwefu;ly")
        self.logger.info("add detsil")

        # AddCustomer

        self.logger.info("1")
        self.Add_cust = AddCustomerPage(self.driver)
        self.logger.info("2")

        self.Add_cust.ClickOnCustomerMenu()
        self.logger.info("3")

        self.Add_cust.ClickOnSubCustomerMenu()
        self.logger.info("4")


        Search_cust=SearchCustomerPage(self.driver)
        self.logger.info("5")
        Search_cust.SetEmail("kiyjcycyhjc676008@gmail.com")
        #Search_cust.SetFirstNAme("Virat")
        self.logger.info("6")
        Search_cust.Clicksearch()
        self.logger.info("7")

        status=Search_cust.searchByEmail("kiyjcycyhjc676008@gmail.com")
        #status=Search_cust.searchByname("Virat Kohli")
        time.sleep(5)
        self.logger.info("8")
        assert True==status




