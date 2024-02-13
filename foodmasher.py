# To allow scraping of HTML
import selenium

# To allow dynamic web fetching
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# To allow waiting
import time

# To get today's date
from datetime import date

# Google Sheets API
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import string

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Get the Google Sheet ready to be written to
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('foodmash-412423-3d34ef97703f.json',scope)
client = gspread.authorize(creds)

# Opening the worksheet and teeing it up
sheet = client.open('foodmash2.0')
sheet_instance = sheet.worksheet('Big Data')

# Writing out all of the dining websites URLs
websites_list = [
    'https://dining.columbia.edu/content/john-jay-dining-hall',
    'https://dining.columbia.edu/content/jjs-place-0',
    'https://dining.columbia.edu/content/ferris-booth-commons-0',
    'https://dining.columbia.edu/chef-mikes',
    'https://dining.columbia.edu/content/chef-dons-pizza-pi',
    'https://dining.columbia.edu/content/faculty-house-0',
    'https://dining.columbia.edu/content/grace-dodge-dining-hall-0',
    'https://dining.columbia.edu/content/fac-shack'
]

# Writing the names of the dining websites
names_list = [
    'John Jay Dining Hall',
    'JJs Place',
    'Ferris Booth Commons',
    'Chef Mikes Sub Shop',
    'Chef Dons Pizza Pi',
    'Faculty House Dining',
    'Grace Dodge Dining Hall',
    'Fac Shack'
]

#Creating a results list for the food selections
results_list = []

for i in range(7):
    
    # Navigate to the dining.columbia.edu website
    driver.get(websites_list[i])

    # Wait for all elements to load because it's a dynamic page
    time.sleep(5)

    # Find all elements with class 'h5'
    elements = driver.find_elements(By.TAG_NAME, "h5")

    # Adding Dining Hall name and today's date to the list
    results_list.append(names_list[i])
    results_list.append(str(date.today()))

    # Put all of the food values in a list
    for el in elements:

        results_list.append(el.text)

    # Append values to the Google Sheet
    sheet_instance.append_rows(values=[results_list])

    # Clear the list for the next iteration
    results_list = []

# Close the browser window
driver.quit()