import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    global Driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    Driver=webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.google.com/")
    yield
    print("This is last test case......")
    
    
    
    
    
    