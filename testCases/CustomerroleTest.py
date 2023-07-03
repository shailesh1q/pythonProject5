from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.CustomerRolePage import CustomerRolePage

class CustomerRole:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def Test4(self,setup):
        self.driver=setup
        self.driver.get(self.baseUrl)

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #



