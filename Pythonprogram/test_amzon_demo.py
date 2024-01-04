import time

from openpyxl.workbook.workbook import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_AmazonDataValidation():
    def test_amazondatavalidation(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        Product="samsung mobile"
        Driver=webdriver.Chrome(options=options)
        Driver.maximize_window()
        Driver.implicitly_wait(30)
        Driver.get("https://www.amazon.in/")
        Driver.find_element(By.ID,"twotabsearchtextbox").send_keys(Product)
        time.sleep(2)
        Driver.find_element(By.ID,"nav-search-submit-button").click()
        time.sleep(2)
        Driver.find_element(By.XPATH,"(//i[@class='a-icon a-icon-checkbox'])[4]").click()
        time.sleep(2)
        allphone=Driver.find_elements(By.XPATH,"//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']")
        allprice=Driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
        
        
        myphone=[]
        myprice=[]
        
        
        for name in allphone:
            myphone.append(name.text)
            
            
        for price in allprice:
            myprice.append(price.text)
            
      
    
        Finalisst=zip(myphone,myprice)
        
        wb=Workbook()
        wb["Sheet"].title="Products Details"
        sh=wb.active
        sh.append(['Mobile Name',"Mobile Price"])
        for i in list(Finalisst):
            sh.append(i)
            
            
        wb.save("Amazon Product Detaills.xlsx")
        wb.close()
        time.sleep(4)
        Driver.close()
        
        
a=Test_AmazonDataValidation()
a.test_amazondatavalidation()
























































































































        
        
                    