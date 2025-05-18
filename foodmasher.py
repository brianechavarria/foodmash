# To allow undetected scraping of HTML
from seleniumbase import SB

""" # To allow dynamic web fetching
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait """

# To allow waiting
import time

# To get today's date
from datetime import date

# Google Sheets API
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import string

# Simple enough, don't really need a function for this
""" def open_the_turnstile_page(sb, url_link):
    url = url_link
    sb.driver.uc_open_with_reconnect(url, reconnect_time=5) """

def click_turnstile_and_verify(sb):
    sb.switch_to_frame("iframe")
    sb.driver.uc_click("span")
    sb.assert_element("img#captcha-success", timeout=3)

""" # Create a new instance of the Chrome driver
driver = webdriver.Chrome() """

# Get the Google Sheet ready to be written to
scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name('glossy-beach-456620-s8-9f8aa8d160d4.json',scope)
client = gspread.authorize(creds)

# Opening the worksheet and teeing it up
sheet = client.open('foodmash3.0')
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

with SB(uc=True, test=True) as sb:
    
    for i, url in enumerate(websites_list):
        
        # Open website
        sb.driver.uc_open_with_reconnect(url, reconnect_time=5)
        
        # If Cloudflare verification exists, bypass it
        if sb.is_element_present("iframe"):
            try:
                click_turnstile_and_verify(sb)
                sb.switch_to_default_content()  # Important: Return to main content
            except Exception as e:
                print(f"CAPTCHA handling failed: {str(e)}")
                sb.switch_to_default_content()

        # Wait some more just for the heck of it
        time.sleep(2)

        # Proceed with grabbing details from the page
        elements = sb.find_elements("h5")
        for e in elements:
            sheet_instance.append_rows(values=[[str(date.today()), names_list[i], e.text]])

""" for i in range(8):
    
    # Navigate to the dining.columbia.edu website
    driver.get(websites_list[i])

    # Wait for all elements to load because it's a dynamic page
    time.sleep(2)
    time.sleep(20)

    # Find all elements with class 'h5'
    elements = driver.find_elements(By.TAG_NAME, "h5")

    # Put all of the food values in a list
    for e in elements:
        sheet_instance.append_rows(values=[[str(date.today()), names_list[i], e.text]]) """
        

""" # Close the browser window
driver.quit()

#test """
