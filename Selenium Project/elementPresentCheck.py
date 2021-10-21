import os
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))  
from utilities.handy_wrappers import HandyWrappers



class Element_Preset_Check():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)
        
        Element_Preset = hw.isElementPresent("//input[@id='name']", By.XPATH)
        print(Element_Preset)
        sleep(3)
        Element_Preset1 = hw.elementPresenceCheck('name', By.ID)
        print(Element_Preset1)
        sleep(3)
        
        
ff = Element_Preset_Check()
ff.test()        