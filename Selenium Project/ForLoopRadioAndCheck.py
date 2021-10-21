from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RadioAndCheckForLoop():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        
        radioList = driver.find_elements(By.XPATH, '//*[@type="radio"]')
        size = len(radioList)
        print('Radio list: ' + str(size))
        for radio in radioList:
            isSelected = radio.is_selected()
            if not isSelected:
                radio.click()
                sleep(1)
                
        checkList = driver.find_elements(By.XPATH, '//*[@type="checkbox"]')
        size = len(checkList)
        print('Radio list: ' + str(size))
        for check in checkList:
            isSelected = check.is_selected()
            if not isSelected:
                check.click()
                sleep(1) 
                


ff = RadioAndCheckForLoop()
ff.test()