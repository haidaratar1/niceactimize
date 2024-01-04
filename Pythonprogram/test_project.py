import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Dropdown:
    def test_dropdown(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        Driver=webdriver.Chrome(options=options)
        Driver.maximize_window()
        Driver.implicitly_wait(30)
        Driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        Driver.find_element(By.ID,"dropdown-class-example").click()
        time.sleep(2)
        alloption=Driver.find_elements(By.XPATH,"//select[@id='dropdown-class-example']/option")
        print("The total number of option is:-",len(alloption))
        
        
        for i in alloption:
            if i.text=="Option2":
                i.click()
                
                
        time.sleep(1)
        Driver.find_element(By.XPATH,"//legend[text()='Dropdown Example']").click()
        
        time.sleep(1)
        Driver.find_element(By.ID,"checkBoxOption2").click()
        time.sleep(2)
        Driver.find_element(By.ID,"checkBoxOption3").click()
        wait=WebDriverWait(Driver,10)
        wait.until(EC.visibility_of_element_located((By.ID,"autocomplete")))
        Driver.find_element(By.ID,"autocomplete").send_keys("Ind")
        allcountry=Driver.find_elements(By.XPATH,"//ul[@id='ui-id-1']/li")
        print("The total number of country:-",len(allcountry))
        
        for coun in allcountry:
            time.sleep(2)
            if coun.text=="India":
                coun.click()
                
                
        radio=Driver.find_elements(By.XPATH,"(//input[@name='radioButton'])")
        print("The total number of radio button:-",len(radio))
        
        for i in range(0,len(radio)):
            time.sleep(2)
            radio[1].click()
            
        
       
        
        time.sleep(2)
        Driver.find_element(By.ID,"alertbtn").click()
        time.sleep(1)
        a=Driver.switch_to.alert
        print(a.text)
        time.sleep(2)
        a.accept()

        
        
        
            
                
                
drop=Test_Dropdown()
drop.test_dropdown()



















      
        
                
        
        
        
        
        
                
        
                
                
                
        
        
        
        
        
        
        









