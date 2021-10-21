from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ClickAndSendKeys():
    
    def test(self):
        baseUrl = 'https://www.google.com/'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        
        searchKeys = driver.find_element(By.NAME, 'q')
        searchKeys.send_keys('Bangladesh')
        sleep(3)

ff = ClickAndSendKeys()
ff.test()