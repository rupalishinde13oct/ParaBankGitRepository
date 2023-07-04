from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class RegistrationPage:

    Xpath_RegisterLink = (By.XPATH , "//a[normalize-space()='Register']")
    Xpath_FirstName = (By.NAME , "customer.firstName")
    Xpath_LastName = (By.NAME , "customer.lastName")
    Xpath_Address = (By.NAME, "customer.address.street")
    Xpath_City = (By.NAME, "customer.address.city")
    Xpath_State = (By.NAME, "customer.address.state")
    Xpath_ZipCode = (By.NAME, "customer.address.zipCode")
    Xpath_PhoneNumber = (By.NAME, "customer.phoneNumber")
    Xpath_SSN = (By.NAME, "customer.ssn")
    Xpath_UserName = (By.NAME, "customer.username")
    Xpath_Password = (By.NAME, "customer.password")
    Xpath_ConfirmPassword = (By.NAME, "repeatedPassword")
    Xpath_RegisterButton = (By.XPATH, "//input[@value='Register']")
    Xpath_Success_Stsus = (By.XPATH , "//p[contains(text(),'Your account was created successfully. You are now')]")


    def __init__(self , d):
        self.d = d

    def Click_RegistrationLink(self):
        self.d.find_element(*RegistrationPage.Xpath_RegisterLink).click()


    def Enter_FirstName(self , fname):
        self.d.find_element(*RegistrationPage.Xpath_FirstName).send_keys(fname)

    def Enter_LastName(self , lname):
        self.d.find_element(*RegistrationPage.Xpath_LastName).send_keys(lname)

    def Enter_Address(self , address):
        self.d.find_element(*RegistrationPage.Xpath_Address).send_keys(address)

    def Enter_City(self , city):
        self.d.find_element(*RegistrationPage.Xpath_City).send_keys(city)

    def Enter_State(self , state):
        self.d.find_element(*RegistrationPage.Xpath_State).send_keys(state)

    def Enter_ZIP_Code(self , zip):
        self.d.find_element(*RegistrationPage.Xpath_ZipCode).send_keys(zip)

    def Enter_Phone_Number(self , phoneno):
        self.d.find_element(*RegistrationPage.Xpath_PhoneNumber).send_keys(phoneno)

    def Enter_SSN(self , ssn):
        self.d.find_element(*RegistrationPage.Xpath_SSN).send_keys(ssn)

    def Enter_Username(self , username):
        self.d.find_element(*RegistrationPage.Xpath_UserName).send_keys(username)

    def Enter_Password(self , password):
        self.d.find_element(*RegistrationPage.Xpath_Password).send_keys(password)

    def Confirm_Password(self , confirmPassword):
        self.d.find_element(*RegistrationPage.Xpath_ConfirmPassword).send_keys(confirmPassword)

    def Click_Register_Button(self):
        self.d.find_element(*RegistrationPage.Xpath_RegisterButton).click()

    def Success_Status(self):
        try:
            if self.d.find_element(*RegistrationPage.Xpath_Success_Stsus):
                return True
            else:
                return False
        except NoSuchElementException:
            pass