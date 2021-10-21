from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class ClickAndSendKeys():
    
    def test(self):
        baseUrl = 'https://letskodeit.teachable.com/'
        driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
        driver.maximize_window()
        driver.get(baseUrl)
        
        #click login link
        clickLink = driver.find_element(By.XPATH, "//a[contains(text(),'Login')]")
        clickLink.click()
        sleep(5)
        email = driver.find_element(By.ID, 'user_email')
        email.send_keys('1234567')
        sleep(3)
        
        password = driver.find_element(By.ID, 'user_password')
        password.send_keys('rashidul@gmail.com')
        sleep(3)
        
        email.clear()
        sleep(3)
  
        email.send_keys('rashidul@gmail.com')
        sleep(3)
        
        
       
        
        
        
        

ff = ClickAndSendKeys()
ff.test()

# class BrowserInteraction():
    
#     def test(self):
#         baseUrl = 'https://letskodeit.teachable.com/p/practice'
#         driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
#         #maximize windows
#         driver.maximize_window()
#         driver.get(baseUrl)
#         #get title
#         title = driver.title
#         print('This is a page titel:' + title)
        
#         #current Url
#         currentUrl = driver.current_url
#         print('This is a page url:' + currentUrl)
        
#         #refress
#         driver.refresh()
#         print('refress last time')
#         driver.get(driver.current_url)
#         print('refress 2nd time')
        
#         #open another url
#         driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
#         #browser back
#         driver.back()
#         print('go one step back')
#         #Forward
#         driver.forward()
#         print('Go One Step Forward')
        
#         #pageSource
#         pageSource = driver.page_source
#         print(pageSource)
        
#         driver.quit()
        
        
        
        

# ff = BrowserInteraction()
# ff.test()

