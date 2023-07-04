from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AccountOverview:

    XPATH_Click_On_AccountOverview = (By.XPATH , "//a[normalize-space()='Accounts Overview']")


    def __init__(self , d):
        self.d = d

    def Click_On_AccountOverview(self):
        self.d.find_element(*AccountOverview.XPATH_Click_On_AccountOverview).click()


    def Success_Message(self):
        try:
            self.d.find_element(By.XPATH, "//a[normalize-space()='Accounts Overview']")

            for i in range(1 , 3):
                amt = self.d.find_element(By.XPATH , "//body/div[1]/div[3]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr["+str(i)+"]/td[2]").text
                print(amt)
        except NoSuchElementException:
            pass