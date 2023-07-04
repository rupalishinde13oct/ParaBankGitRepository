import pytest
from selenium.webdriver.common.by import By

from PageObjects.AccountOverview import AccountOverview
from PageObjects.LoginPage import LoginPage
from Utilities.reagConfig import ReadConfig

class TestAccountOverview:

    url = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    @pytest.mark.skip
    def test_AccountOverview_007(self , setup):
        self.d = setup

        self.d.get(self.url)
        self.lp = LoginPage(self.d)
        self.lp.EnterUsername(self.username)
        self.lp.EnterPassword(self.password)
        self.lp.Click_Login_Button()

        self.ao = AccountOverview(self.d)
        self.ao.Click_On_AccountOverview()




        # self.ao.Success_Message()