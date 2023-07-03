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


class Test_oo3_AddCustomer:
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
        self.Add_cust.clickAddNewCustomer()
        self.logger.info("5")

        self.email=random_generator() + "@gmail.com"
        self.Add_cust.SetEmail(self.email)
        self.logger.info("6")
        self.Add_cust.SetPassword("test123")
        self.logger.info("7")

        self.Add_cust.SetFirstName("shaielsh")
        self.Add_cust.SetLastName("bhavsar")
        self.logger.info("8")

        self.Add_cust.SetGender("Male")
        self.logger.info("9")
        self.Add_cust.SetDOB("01/01/1980")
        self.logger.info("10")
        self.Add_cust.SetCopanyname("hp")
        # self.Add_cust.SetNewsletter("Test store 2")



        self.logger.info("11")
        self.Add_cust.SetNewsletter("Test store 2")
        self.logger.info("13")

        self.Add_cust.SetCustomerRole("Guests")
        self.logger.info("12")






        self.Add_cust.SetManagerOfVendor("Vendor 2")
        self.Add_cust.SetAdmincontent("love boy")
        self.Add_cust.ClickOnSave()

        self.logger.info("saving custoemr info")
        self.logger.info("add csutomer validation")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)
        self.logger.info("final before")

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("add custoemr tested")
        else:
            self.driver.save_screenshot(".\\ScreenShorts\\" + "test_addcustomerPAge.png")
            assert True == False
            self.logger.info("add customer failed")
        self.driver.close()
        self.logger.info("final")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
