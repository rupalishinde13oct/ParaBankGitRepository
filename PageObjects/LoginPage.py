from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage:

    Name_UserName = (By.XPATH , "//input[@name='username']")
    Name_Password = (By.XPATH , "//input[@name='password']")
    Xpath_Login_Button = (By.XPATH , "//input[@value='Log In']")
    Xpath_Logout_Button = (By.XPATH , "//a[normalize-space()='Log Out']")
    Xpath_Success_Msg = (By.XPATH , "//h1[normalize-space()='Accounts Overview']")


    def __init__(self , d):
        self.d = d

    def EnterUsername(self , username):
        self.d.find_element(*LoginPage.Name_UserName).send_keys(username)

    def EnterPassword(self , password):
        self.d.find_element(*LoginPage.Name_Password).send_keys(password)

    def Click_Login_Button(self):
        self.d.find_element(*LoginPage.Xpath_Login_Button).click()

    def Click_Logout(self):
        self.d.find_element(*LoginPage.Xpath_Logout_Button).click()

    def Success_Status(self):
        try:
            if self.d.find_element(*LoginPage.Xpath_Success_Msg):
                return True
            else:
                return False
        except NoSuchElementException:
            pass
