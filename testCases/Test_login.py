
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseUrl = ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()


    def test_Home_Page_title(self,setup):
        self.logger.info("****test_001********")
        self.logger.info("***verifying homepage title******")
        self.driver=setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***passed***")

        else:
            self.driver.save_screenshot(".\\ScreenShorts\\"+"Home_Page_Title.png")
            self.driver.close()
            self.logger.info("******failed*****")
            assert False


    def test_login(self,setup):
        self.logger.info("**testlogin**")
        self.logger.info("*****varifyn****")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******8passed*******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\ScreenShorts\\" + "test_login.png")
            self.driver.close()
            self.logger.info("*****failed****")
            assert False

