from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class OpenAccount:

    XPATH_Click_OpenNewAccLink = (By.XPATH , "//a[@href='/parabank/openaccount.htm']")
    XPATH_Select_SavingACCType = (By.XPATH , "//select[@id='type']")
    XPATH_Select_ACCNumber = (By.XPATH , "//select[@id='fromAccountId']")
    XPATH_Click_CreateAccount = (By.XPATH , "//input[@type='submit']")
    XPATH_Success_MSG = (By.XPATH , "//h1[@class='title']")

    def __init__(self , d):
        self.d = d
        self.wait = WebDriverWait(d , 10 , poll_frequency=0.2)

    def Click_On_Open_NewAccountLink(self):
        self.d.find_element(*OpenAccount.XPATH_Click_OpenNewAccLink).click()

    def Select_AccountType(self):
        Select(self.d.find_element(*OpenAccount.XPATH_Select_SavingACCType)).select_by_visible_text("SAVINGS")

    def Select_AccountNo(self):
        # self.wait.until(expected_conditions.presence_of_element_located(self.XPATH_Select_ACCNumber))
        Select(self.d.find_element(*OpenAccount.XPATH_Select_ACCNumber)).select_by_index(0)


    def Click_On_CreateAccount(self):
        # self.wait.until(expected_conditions.presence_of_element_located(self.XPATH_Click_CreateAccount))
        self.d.find_element(*OpenAccount.XPATH_Click_CreateAccount).click()

    def Success_MSG(self):
        try:
            # self.wait.until(expected_conditions.presence_of_element_located(self.XPATH_Success_MSG))
            self.d.find_element(*OpenAccount.XPATH_Success_MSG)
            print(self.d.find_element(*OpenAccount.XPATH_Success_MSG).text)
            print(self.d.find_element(By.XPATH , "//p[normalize-space()='Congratulations, your account is now open.']").text)
            print(self.d.find_element(By.XPATH , "//b[normalize-space()='Your new account number:']").text)
            print(self.d.find_element(By.XPATH , "//a[@id='newAccountId']").text)
            return True

        except NoSuchElementException:
            return False






