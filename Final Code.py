from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open the initial page
driver.get('https://abpp.org/directory/?pagenum=6')
time.sleep(2)

# Loop through the pages
while True:
    # Find the table on the current page
    table = driver.find_element(By.XPATH, '//*[@id="gv-view-31715-1"]/div[2]/table')

    # Open the CSV file in append mode
    with open('psychology4566123_doc.csv', 'a', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Find the rows in the table
        rows = table.find_elements(By.XPATH, './/tbody/tr')
    
        # Extract data from each row
        for row in rows:
            try:
                first_name = row.find_element(By.XPATH, './/*[@id="gv-field-246-2.3"]/a').text.replace(",", " ")
            except:
                first_name = ""
            try:
                last_name = row.find_element(By.XPATH, './/*[@id="gv-field-246-2.6"]/a').text.replace(",", " ")
            except:
                last_name = ""
            try:
                address = row.find_element(By.XPATH, './/td[@data-label="Address"]').text.replace(",", " ")
            except:
                address = ""
            try:
                contact = row.find_element(By.XPATH, './/td[@data-label="Contact"]').text.replace(",", " ")
            except:
                contact = ""
            try:    
                licensed_in = row.find_element(By.XPATH, './/*[@id="gv-field-246-8"]/ul').text.replace(",", " ")
            except:
                licensed_in = ""
                
            # Write data to the CSV file
            csv_writer.writerow([first_name, last_name, address, contact, licensed_in])
    
    # Check if there is a next button
    next_button = driver.find_element(By.XPATH, '//a[@class="next page-numbers"]')
    if not next_button.is_enabled():
        print("Your job is done! Thanks")
        break
    
    # Click on the next button
    next_button.click()
    
    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.staleness_of(table))
    
    # Wait for a brief moment to ensure all elements are loaded
    time.sleep(2)
