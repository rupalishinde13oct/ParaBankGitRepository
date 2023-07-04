import pytest
from selenium import webdriver

@pytest.fixture(params=[
    ("Rupali" , "124578" , "Pass"),
    ("Rupali11" , "124578" , "Fail"),
    ("Rupali" , "1245781", "Fail"),
    ("Rupali1" , "1245781", "Fail")
])

def getLoginData(request):
    return request.param



def pytest_addoption(parser):
    return parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        print("Launching Chrome Browser...")
        d = webdriver.Chrome()

    elif browser == 'firefox':
        print("Launching Firefox Browser...")
        d = webdriver.Firefox()

    elif browser == 'edge':
        print("Launching Edge Browser...")
        d = webdriver.Edge()

    else:
        print("Headless Mode..")
        # opt = webdriver.ChromeOptions()
        # opt.add_argument("headless")
        # d = webdriver.Chrome(options=opt)
        d = webdriver.Chrome()
    d.maximize_window()
    return d