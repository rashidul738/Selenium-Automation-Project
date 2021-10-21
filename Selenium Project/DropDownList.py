from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class DropDownList():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        
        element = driver.find_element(By.ID, 'carselect')
        sel = Select(element)
        sel.select_by_value('benz')
        print('select benz by value')
        sleep(2)
        
        sel.select_by_index('2')
        print('select honda by index')
        sleep(2)
        
        sel.select_by_visible_text('BMW')
        print('select BMW by visible_text')
        sleep(2)
        
        sel.select_by_index(2)
        print('select honda by index - 2')
        sleep(2)
        
        
        
                
ff = DropDownList()
ff.test()                