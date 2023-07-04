import time
from Utilities.Logger import Logger
from PageObjects.LoginPage import LoginPage
from Utilities.reagConfig import ReadConfig

class TestLogin:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log = Logger.logGen()

    def test_Login_003(self , setup):
        self.log.info("test_Login_003 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)
        self.lp = LoginPage(self.d)

        self.lp.EnterUsername(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.EnterPassword(self.password)
        self.log.info("Entering Password-->" + self.password)
        self.lp.Click_Login_Button()
        self.log.info("Clicking on Login Button")
        if self.lp.Success_Status() == True:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_Login_003_Pass.png")
            self.log.info("test_Login_003 is Passed")
            self.lp.Click_Logout()
            self.log.info("Click on Logout")
            assert True
        else:
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_Login_003_Fail.png")
            self.log.info("test_Login_003 is Failed")
            assert False
        self.log.info("test_Login_003 is Completed")
