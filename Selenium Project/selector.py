from selenium import webdriver
from selenium.webdriver.common.by import By


class ListOfElement():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.get(baseUrl)
        
        elementListByClass = driver.find_elements_by_class_name('inputs')
        lenght = len(elementListByClass)
        if elementListByClass is not None:
            print('we found an element is: ' + str(lenght))
        
        elementListByTag = driver.find_elements(By.TAG_NAME, "th")
        lenght1 = len(elementListByTag)
        if elementListByTag is not None:
            print('we found an element is: ' + str(lenght1))    

ff = ListOfElement()
ff.test()         


# class ByDemo():
    
#     def test(self):
#         baseUrl = 'https://letskodeit.teachable.com/p/practice'
#         driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
#         driver.get(baseUrl)
        
#         elementById = driver.find_element(By.ID, "name")
#         if elementById is not None:
#             print('we found an element by ID')
        
#         elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
#         if elementByXpath is not None:
#             print('we found an element by Xpath')    
            
#         elementByLinkText = driver.find_element(By.LINK_TEXT, "Login")
#         if elementByLinkText is not None:
#             print('we found an element By Link Text')            
        
        
        
# ff = ByDemo()
# ff.test()
