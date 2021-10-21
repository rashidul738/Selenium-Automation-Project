from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



baseUrl = 'https://www.ryanscomputers.com/category/notebook-all-notebook'
driver = webdriver.Chrome(executable_path="G:\Projects\SeleNium\chromedriver.exe")
driver.maximize_window()
driver.get(baseUrl)

selector = '//a[@class="product-title-grid"]'
links = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, selector)))

# for link in links:
#     print(link)
    
for i in range(3):
    links = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.XPATH, selector)))
    links[i].click()
    
    school = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'title')))
    print(school.text)
    driver.back()
driver.quit()    
        
                
