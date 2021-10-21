from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class RadioBatton():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        
        radio = driver.find_element(By.ID, 'benzradio')
        radio.click()
        sleep(1)
        
        radio1 = driver.find_element_by_xpath("//input[@id='bmwradio']")
        radio1.click()
        sleep(1)
        
        radio2 = driver.find_element(By.ID, 'hondaradio')
        radio2.click()
        sleep(1)
        
        check1 = driver.find_element(By.ID, 'bmwcheck')
        check1.click()
        sleep(1)
        
        check2 = driver.find_element(By.ID, 'benzcheck')
        check2.click()
        sleep(1)
        
        check3 = driver.find_element(By.ID, 'hondacheck')
        check3.click()
        sleep(1)
        
        print("BMW radio Button is selected? " + str(radio1.is_selected()))
        print("BMW radio Button is selected? " + str(radio2.is_selected()))
        print("BMW radio Button is selected? " + str(radio.is_selected()))
        
        
        print("BMW radio Button is Checked? " + str(check1.is_selected()))
        print("BMW radio Button is Checked? " + str(check2.is_selected()))
        print("BMW radio Button is Checked? " + str(check3.is_selected()))
        
        
        

ff = RadioBatton()
ff.test()