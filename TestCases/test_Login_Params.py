import time

from PageObjects.LoginPage import LoginPage
from Utilities.Logger import Logger
from Utilities.reagConfig import ReadConfig

class TestLoginParam:
    url = ReadConfig.getURL()
    log = Logger.logGen()

    def test_Login_Params_004(self , setup , getLoginData):

        self.log.info("test_Login_Params_004 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)
        self.lp = LoginPage(self.d)

        self.lp.EnterUsername(getLoginData[0])
        self.log.info("Entering Username-->" + getLoginData[0])
        self.lp.EnterPassword(getLoginData[1])
        self.log.info("Entering Password-->" + getLoginData[1])
        self.lp.Click_Login_Button()
        time.sleep(2)
        self.log.info("Clicking on Login Button")

        if self.lp.Success_Status() == True:
            if getLoginData[2] == 'Pass':
                self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+getLoginData[0]+"__"+getLoginData[1]+"test_Login_Params_004_Pass.png")
                self.log.info("test_Login_Params_004 is Passed")
                self.lp.Click_Logout()
                self.log.info("Click on Logout")
                assert True
            else:
                self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+getLoginData[0]+"__"+getLoginData[1]+"test_Login_Params_004_Fail.png")
                self.log.info("test_Login_Params_004 is Failed")
                assert False
        else:
            if getLoginData[2] == 'Fail':
                self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+getLoginData[0]+"__"+getLoginData[1]+"test_Login_Params_004_Pass.png")
                self.log.info("test_Login_Params_004 is Passed")
                assert True
            else:
                self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+getLoginData[0]+"__"+getLoginData[1]+"test_Login_Params_004_Fail.png")
                self.log.info("test_Login_Params_004 is Failed")
                assert False

        self.log.info("test_Login_Params_004 is Completed")