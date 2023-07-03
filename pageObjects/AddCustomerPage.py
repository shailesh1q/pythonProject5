import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomerPage:
    lnkCustomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_subMenu_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"

    btnAddNew_xpath="//a[@class='btn btn-primary']"

    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"

    rdGender_male_xpath="//input[@id='Gender_Male']"
    rdGender_female_xpath="//input[@id='Gender_Female']"
    txtDOB_xpath="//input[@id='DateOfBirth']"
    txtCompany_Name_xpath="//input[@id='Company']"
    txtAdmin_context_xpath="//textarea[@id='AdminComment']"

    txt_Customer_role_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstItemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstItemAdministrator_xpath="//li[contains(text(),'Administrators')]"
    lstItemGuest_xpath="//li[contains(text(),'Guests')]"
    lstItemVendor_xpath="//li[contains(text(),'Vendors')]"

    drp_managerOf_vendor="//*[@id='VendorId']"
    btnSave_xpath="//button[@name='save']"

    lst_newsletter_xpath="(//div[@role='listbox'])[1]"
    lstItem_news_Test_Store_xpath="//li[contains(text(),'Test store 2')]"
    lstItem_news_your_store_xpath="//li[contains(text(),'Your store name')]"







    def __init__(self,driver):
        self.driver=driver


    def ClickOnCustomerMenu(self):
        #self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).clear()
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()

    def ClickOnSubCustomerMenu(self):
       # self.driver.find_element(By.XPATH,self.lnkCustomer_subMenu_xpath).clear()
        self.driver.find_element(By.XPATH, self.lnkCustomer_subMenu_xpath).click()

    def clickAddNewCustomer(self):
        self.driver.find_element(By.XPATH,self.btnAddNew_xpath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def SetPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def SetFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(firstname)

    def SetLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lastname)

    def SetGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH, self.rdGender_male_xpath).click()

        elif gender == "Female":
            self.driver.find_element(By.XPATH, self.rdGender_female_xpath).click()
        else:
            self.driver.find_element(By.ID, self.rdGender_male_xpath).click()


    def SetDOB(self,dob):
        self.driver.find_element(By.XPATH,self.txtDOB_xpath).send_keys(dob)

    def SetCopanyname(self,companyName):
        self.driver.find_element(By.XPATH,self.txtCompany_Name_xpath).send_keys(companyName)
    def SetManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_managerOf_vendor))
        drp.select_by_visible_text(value)




    def SetCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txt_Customer_role_xpath).click()
       # self.lstItem = self.driver.find_element(By.XPATH, self.lstItemGuest_xpath)
        time.sleep(3)
        if role == 'Registered':
            self.lstItem = self.driver.find_element(By.XPATH, self.lstItemRegistered_xpath)
        elif role == 'Administrators':
            self.lstItem=self.driver.find_element(By.XPATH,self.lstItemAdministrator_xpath)
        elif role== 'Guests':
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstItem=self.driver.find_element(By.XPATH,self.lstItemGuest_xpath)
        elif role=='Registered':
            self.lstItem=self.driver.find_element(By.XPATH,self.lstItemRegistered_xpath)
        elif role=='Vendors':
            self.lstItem=self.driver.find_element(By.XPATH,self.lstItemVendor_xpath)
        else:
            self.driver.find_element(By.XPATH,self.lstItemGuest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.lstItem)

    def SetNewsletter(self,store):
        self.driver.find_element(By.XPATH, self.lst_newsletter_xpath).click()
        time.sleep(3)
        if store=='Your store name':
            self.newsItem=self.driver.find_element(By.XPATH,self.lstItem_news_your_store_xpath)
        elif store=='Test store 2':
            self.newsItem=self.driver.find_element(By.XPATH,self.lstItem_news_Test_Store_xpath)
        else:
            self.driver.find_element(By.XPATH,self.lstItem_news_Test_Store_xpath)
        self.driver.execute_script("arguments[0].click();", self.newsItem)


    def SetAdmincontent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdmin_context_xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()

















