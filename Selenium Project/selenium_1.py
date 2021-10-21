from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="G:\products\products\chromedriver.exe")
driver.get('https://directory.ntschools.net/#/schools')

selector = '#search-panel-container .nav-link'
links = WebDriverWait(driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))

school_name_selector = '.school-title h1'

for i in range(10):
    links = WebDriverWait(driver, 60).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector))
    )
    
    links[i].click()
    
    name_e = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, school_name_selector))
    )
    
    print(name_e.text)
    driver.back()


driver.quit()
