from selenium import webdriver
def test_google():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    Driver=webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.google.com/")
    Driver.title=="Google"
    Driver.quit()
    
    
    
def test_gmail():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    Driver=webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.gmail.com/")
    Driver.title=="Gmail"
    Driver.quit()
    
    
def test_Instagram():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    Driver=webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.instagram.com/")
    Driver.title=="Instagram"
    Driver.quit()
    
    
def test_youtube():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    Driver=webdriver.Chrome(options=options)
    Driver.maximize_window()
    Driver.implicitly_wait(30)
    Driver.get("https://www.youtube.com/")
    Driver.title=="YouTube"
    Driver.quit()
    

    
    

    


    
    
    

    

    
    


    
    
    
    

    
    
    

    



    




    
