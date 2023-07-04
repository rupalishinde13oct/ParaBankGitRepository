from Utilities.reagConfig import ReadConfig
from Utilities.Logger import Logger
class TestPageTitle:

    url = ReadConfig.getURL()
    log = Logger.logGen()

    def test_PageTitle_001(self , setup):
        self.log.info("test_PageTitle_001 is Started")
        self.d = setup
        self.log.info("Launching Browser...!!")
        self.d.get(self.url)
        self.log.info("Go to-->" + self.url)

        if self.d.title == "ParaBank | Welcome | Online Banking":
            self.log.info("test_PageTitle_001 is Passed")
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_PageTitle_001_Pass.png")
            self.log.info("Page Title is -->" + self.d.title)
            assert True

        else:
            self.log.info("Page Title is -->" + self.d.title)
            self.log.info("test_PageTitle_001 is Failed")
            self.d.save_screenshot("D:\\Rupali Prathamesh Pandit\\ParaBank\\Screenshots\\test_PageTitle_001_Fail.png")
            assert False

        self.log.info("test_PageTitle_001 is Completed")