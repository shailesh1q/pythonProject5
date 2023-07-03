from selenium import webdriver
from selenium.webdriver.common.by import By


class SearchCustomerPage:
    txt_email_xpath="//input[@id='SearchEmail']"
    txt_firstNAme_xpath="//input[@id='SearchFirstName']"
    txt_lastName_xpath="//input[@id='SearchLastName']"
    btn_search_xpath="// input[ @ id = 'SearchLastName']"

    tableSeacrhResult_xpath = "//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColummns_xpath="//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver=driver
    def SetEmail(self,email):
        #self.driver.find_element(By.XPATH, self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def SetFirstNAme(self,firstName):
        #self.driver.find_element(By.XPATH, self.txt_firstNAme_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_firstNAme_xpath).send_keys(firstName)
    def SetLastName(self,lastname):
        #self.driver.find_element(By.XPATH, self.txt_lastName_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_lastName_xpath).send_keys(lastname)
    def Clicksearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
    def getNoRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))
    def getNoColumns(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColummns_xpath))
    def searchByEmail(self,email):
        flag=False
        for r in range(1,self.getNoRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag = True
                break
        return flag
    def searchByname(self,name):
        flag=False
        for r in range(1,self.getNoRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            Name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==Name:
                flag = True
                break
        return flag


