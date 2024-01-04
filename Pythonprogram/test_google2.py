
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest 


def test_demo(setup):
    Driver=webdriver.Chrome()
    Driver.find_element(By.NAME).send_keys("Haidar")
    
    
    
