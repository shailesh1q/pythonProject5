import time

import  pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis

class Test_002__DDTLogin:

    baseUrl = ReadConfig.getApplicationURL()
    path=".\\TestData\\LoginData.xlsx"
    logger=LogGen.loggen()




    def test_login_ddt(self,setup):
        self.logger.info("******Test_002_DDT_Login**************")
        self.logger.info("*****varifyn****")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)


        self.rows=XLUtilis.getRowCount(self.path,"Sheet1")
        print("nuber of rows",self.rows)

        lst_status=[]   # empty list variable

        for r in range(2,self.rows+1):

            self.user=XLUtilis.readData(self.path,"Sheet1",r,1)

            self.password=XLUtilis.readData(self.path,"Sheet1",r,2)

            self.exp=XLUtilis.readData(self.path,"Sheet1",r,3)


            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*******Passed****")
                    self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***Failed***")
                    self.lp.clickLogout();
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("***Failed****")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****PAssed*")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("******8Logging DDT passed")
            self.driver.close()
            assert True

        else:
            self.logger.info("****DDT Failed*8")
            self.driver.close()
            assert False

        self.logger.info("***End LOGIN DDT*****")
        self.logger.info("*****test_002 colpletred****8")










        #
        # self.lp.clickLogin()
        # act_title=self.driver.title
        # if act_title== exp_title:
        #     assert True
        #     self.logger.info("******8passed*******")
        #     self.driver.close()
        #
        # else:
        #     self.driver.save_screenshot(".\\ScreenShorts\\" + "test_login.png")
        #     self.driver.close()
        #     self.logger.info("*****failed****")
        #     assert False

