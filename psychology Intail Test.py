from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://abpp.org/directory/')
time.sleep(2)

tabe=driver.find_elements(By.XPATH,'//*[@id="gv-view-31715-1"]/div[2]/table')

for i in tabe:
    csv_writer = open('psychology_doc.csv','a',encoding='utf-8')
    row=driver.find_elements(By.XPATH,'//*[@id="gv-view-31715-1"]/div[2]/table/tbody/tr')
    
    
    for data in row:
        try:
            first_name=data.find_element(By.XPATH,'.//*[@id="gv-field-246-2.3"]/a').text.replace(","," ")
        except:
            first_name=""
        try:
            last_name=data.find_element(By.XPATH,'.//*[@id="gv-field-246-2.6"]/a').text.replace(","," ")
        except:
            last_name=""
        try:
            adress=data.find_element(By.XPATH,'.//td[@data-label="Address"]').text.replace(","," ")
        except:
            adress=""
        try:
            Contact=data.find_element(By.XPATH,'.//td[@data-label="Contact"]').text.replace(","," ")
        except:
            Contact=""  
        try:    
            Licensed_In=data.find_element(By.XPATH,'.//*[@id="gv-field-246-8"]/ul').text.replace(","," ")
        except:
            Licensed_In=""
        csv_writer.write('{},{},{},{},{},\n' .format(first_name,last_name,adress,Contact,Licensed_In))
    csv_writer.close()
next_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@class="next page-numbers"]')))
next_button.click()    
time.sleep(2)       
        
