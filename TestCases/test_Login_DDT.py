import time
from Utilities.Logger import Logger
from PageObjects.LoginPage import LoginPage
from Utilities.reagConfig import ReadConfig
from  Utilities.readXLData import readXLUtil
class TestLoginDDT:

    url = ReadConfig.getURL()
    log = Logger.logGen()
    path = "D:\\Rupali Prathamesh Pandit\\ParaBank\\TestData\\LoginData.xlsx"

    def test_Login_DDT_005(self , setup):
        self.log.info("test_Login_003 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)
        self.lp = LoginPage(self.d)

        self.rows = readXLUtil.getRowCount(self.path , 'Sheet1')
        # print(self.rows)
        for i in range(2 , self.rows+1):
            username = readXLUtil.readXLData(self.path , 'Sheet1' , i , 2)
            password = readXLUtil.readXLData(self.path , 'Sheet1' , i , 3)

            self.lp.EnterUsername(username)
            self.log.info("Entering Username-->" + username)
            self.lp.EnterPassword(password)
            self.log.info("Entering Password-->" + str(password))
            self.lp.Click_Login_Button()
            self.log.info("Clicking on Login Button")
            status_list = []
            if self.lp.Success_Status() == True:

                if readXLUtil.readXLData(self.path , 'Sheet1' , i , 4) == 'Pass':
                    self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+username+"--"+str(password)+"test_Login_DDT_005_Pass.png")
                    status_list.append("Pass")
                    readXLUtil.WriteXLData(self.path , 'Sheet1' , i , 5 , 'Pass')
                    self.lp.Click_Logout()
                    self.log.info("Click on Logout")
                else:
                    self.d.save_screenshot(
                        "D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\"+username+"--"+str(password)+"test_Login_DDT_005_Fail.png")
                    status_list.append("Fail")
                    readXLUtil.WriteXLData(self.path, 'Sheet1', i, 5, 'Fail')

            else:

                if readXLUtil.readXLData(self.path , 'Sheet1' , i , 4) == 'Fail':
                    self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_Login_003_Pass.png")
                    status_list.append("Pass")
                    readXLUtil.WriteXLData(self.path, 'Sheet1', i, 5, 'Fail')
                else:
                    self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_Login_003_Fail.png")
                    status_list.append("Fail")
                    readXLUtil.WriteXLData(self.path, 'Sheet1', i, 5, 'Fail')

            if 'Pass' in status_list:
                assert True
            else:
                assert False

        # self.log.info("test_Login_003 is Completed")
