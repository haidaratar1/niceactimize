import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from openpyxl.reader.excel import load_workbook
from openpyxl import load_workbook


class Test_FacebookLogin:
    def test_facebooklogin(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        Driver=webdriver.Chrome(options=options)
        Driver.maximize_window()
        Driver.implicitly_wait(30)
        Driver.get("https://www.facebook.com/")
        Driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
        time.sleep(2)
        Driver.find_element(By.NAME,"firstname").send_keys("Haidar1")
        time.sleep(2)
        Driver.find_element(By.NAME,"lastname").send_keys("Atar1")
        time.sleep(2)
        Driver.find_element(By.NAME,"reg_email__").send_keys("haidar1.atar@gmail.com")
        time.sleep(2)
        Driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("haidar1.atar@gmail.com")
        time.sleep(2)
        Driver.find_element(By.NAME,"reg_passwd__").send_keys("haidar@123")
        time.sleep(2)
        
        days=Driver.find_element(By.ID,"day")
        day=Select(days)
        day.select_by_visible_text("5")
        
        months=Driver.find_element(By.ID,"month")
        month=Select(months)
        month.select_by_visible_text("Jun")
        
        years=Driver.find_element(By.ID,"year")
        year=Select(years)
        year.select_by_visible_text("2005")
        
        time.sleep(2)
        Driver.find_element(By.XPATH,"//label[text()='Male']").click()
        Driver.find_element(By.XPATH,"(//button[contains(text(),'Sign Up')])[1]").click()
        
        
        
       
face=Test_FacebookLogin()
face.test_facebooklogin()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        