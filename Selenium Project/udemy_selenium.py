from os import name
from selenium import webdriver


class FindByIdName():
    
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")
        if elementById is not None:
            print('we found an element')
        elementByName = driver.find_element_by_name('show-hide')
        if elementByName is not None:
            print('we found an elementByName')            
        
        
        
ff = FindByIdName()
ff.test()        
