from selenium import webdriver
from selenium.webdriver.common.by import By


class CustomerRolePage:
    lnk_customer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnl_customerRole_xpath="//a[@href='#']//p[contains(text(),'Customer roles ')]"
    btn_AddNew_xpath="//a[@class='btn btn-primary']"
    txt_NAME_xpath="//input[@id='Name']"
    txt_systemName_xpath="//input[@id='SystemName']"
    btn_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver
    def ClickCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnk_customer_xpath).click()
    def ClickCustomerROle(self):
        self.driver.find_element(By.XPATH,self.lnl_customerRole_xpath).click()
    def ClickAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_AddNew_xpath).click()
    def SetName(self,name):
        self.driver.find_element(By.XPATH,self.txt_NAME_xpath).send_keys(name)
    def SetSystemName(self,systemName):
        self.driver.find_element(By.XPATH,self.txt_systemName_xpath).send_keys(systemName)
    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()


