import time
from Utilities.Logger import Logger
from PageObjects.LoginPage import LoginPage
from PageObjects.OpenAccount import OpenAccount
from Utilities.reagConfig import ReadConfig
class TestOpenAccount:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Logger.logGen()

    def test_OpenAccount_006(self , setup):
        self.log.info("test_OpenAccount_006 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)

        self.lp = LoginPage(self.d)
        self.lp.EnterUsername(self.username)
        self.log.info("Entering Username-->" +self.username)
        self.lp.EnterPassword(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login_Button()
        self.log.info("Clicking on Login Button")

        self.oc = OpenAccount(self.d)
        self.oc.Click_On_Open_NewAccountLink()
        self.log.info("Click on Open New Account")
        self.oc.Select_AccountType()
        self.log.info("Selecting Account Type")
        self.oc.Select_AccountNo()
        self.log.info("Selecting Account Number")
        time.sleep(2)
        self.oc.Click_On_CreateAccount()
        self.log.info("Clicking on Creat New Account Button")
        time.sleep(2)
        if self.oc.Success_MSG() == True:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_OpenAccount_006_Pass.png")
            self.log.info("test_OpenAccount_006 is Passed")
            assert True
        else:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_OpenAccount_006_Fail.png")
            self.log.info("test_OpenAccount_006 is Failed")
            assert False

        self.log.info("test_OpenAccount_006 is Completed")
