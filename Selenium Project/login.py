import os
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))  
from utilities.handy_wrappers import HandyWrappers


class Login():
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrappers(driver)
        driver.get(baseUrl)
        
        # logins = hw.getElement("//a[contains(text(),'Login')]", locatorType='xpath')
        # #logins = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
        # logins.click()
        # sleep(5)
        
        # email = hw.getElement('user_email', locatorType='id')
        # email.send_keys('test@email.com')
        # sleep(3)
        
        # password = hw.getElement('user_password', locatorType='id')
        # password.send_keys('abcabc')
        # sleep(3)
        # loginButton = hw.getElement('commit', locatorType='name')
        # loginButton.click()
        # sleep(10)
        viewAll = hw.getElement("//a[contains(text(),'View All Courses')]", locatorType='xpath')
        viewAll.click()
        sleep(5)

        cource = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
        courceLocator = cource.format('JavaScript for beginners')
        courceElement = driver.find_element(By.XPATH, courceLocator)
        courceElement.click()
        sleep(4)
                
ff = Login()
ff.test()  