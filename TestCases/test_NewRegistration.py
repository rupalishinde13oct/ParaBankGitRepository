import time

from Utilities.Logger import Logger
from Utilities.reagConfig import ReadConfig
from PageObjects.RegistrationPage import RegistrationPage
class TestRegistrationPage:

    url = ReadConfig.getURL()
    log = Logger.logGen()
    def test_RegistrationPage_002(self , setup):
        self.log.info("test_RegistrationPage_002 is Started")
        self.d = setup
        self.log.info("Launching Browser..!!")
        self.d.get(self.url)
        self.log.info("Go to-->"+ self.url)

        self.rp = RegistrationPage(self.d)

        self.rp.Click_RegistrationLink()
        self.log.info("Clicking on Registration link")
        self.rp.Enter_FirstName("Rupali")
        self.log.info("Entering First Name")
        self.rp.Enter_LastName("Pandit")
        self.log.info("Entering Last Name")
        self.rp.Enter_Address("Satara")
        self.log.info("Entering Address")
        self.rp.Enter_City("Pune")
        self.log.info("Entering City")
        self.rp.Enter_State("Maharashtra")
        self.log.info("Entering State")
        self.rp.Enter_ZIP_Code("123456")
        self.log.info("Entering ZIP Code")
        self.rp.Enter_Phone_Number("9632587412")
        self.log.info("Entering Contact Number")
        self.rp.Enter_SSN("123456")
        self.log.info("Entering SSN number")
        self.rp.Enter_Username("Rupali1122")
        self.log.info("Entering Username")
        self.rp.Enter_Password("124578")
        self.log.info("Entering Passwrd")
        self.rp.Confirm_Password("124578")
        self.log.info("Confirming Password")
        self.rp.Click_Register_Button()
        self.log.info("Clicking On Register Button")

        if self.rp.Success_Status() == True:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_RegistrationPage_002_Pass.png")
            self.log.info("test_RegistrationPage_002 is Passed")
            assert True
        else:
            self.d.save_screenshot(
                "D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_RegistrationPage_002_Fail.png")
            self.log.info("test_RegistrationPage_002 is Failed")
            assert False

        self.log.info("test_RegistrationPage_002 is Completed")

