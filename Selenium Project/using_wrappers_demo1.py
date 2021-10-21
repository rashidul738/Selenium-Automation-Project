import os
import sys
from time import sleep
from selenium import webdriver
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))  
from utilities.handy_wrappers import HandyWrappers


class UsingWrappers():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)
        
        # TextField = hw.getElement('name')
        # TextField.send_keys('Test')
        # sleep(3)
        
        # TextField = hw.getElement("//input[@id='name']", locatorType='xpath')
        # TextField.send_keys('Test')
        # sleep(3)
        
        course = hw.getElement('//div[@class="row"]/a/@href', locatorType='xpath')
        course.click()
        sleep(3)

        
        
        
                
ff = UsingWrappers()
ff.test()  