from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class GetText():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        
        openTabElement = driver.find_element_by_id('opentab')
        element_text = openTabElement.text
        print(element_text)
        sleep(3)
        
        
        
                
ff = GetText()
ff.test()    