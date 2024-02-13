import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


urls = ["https://dining.columbia.edu/content/john-jay-dining-hall"]
        # "https://dining.columbia.edu/content/jjs-place-0",
        # "https://dining.columbia.edu/content/ferris-booth-commons-0",
        # "https://dining.columbia.edu/chef-mikes",
        # "https://dining.columbia.edu/content/faculty-house-0",
        # "https://dining.columbia.edu/content/chef-dons-pizza-pi",
        # "https://dining.columbia.edu/content/grace-dodge-dining-hall-0",
        # "https://dining.columbia.edu/content/fac-shack"]

# for url in urls:
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, features="html.parser")
#     data = soup.find_all("div",{"class":"meal-items"})
#     for d in data:
#         print(d)
#         print("  ")



service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://dining.columbia.edu/content/ferris-booth-commons-0")
driver.implicitly_wait(10)
menu = driver.find_element("xpath", '//*[@id="cu-dining-meals"]/div/div')

base_xpath = '//*[@id="cu-dining-meals"]/div/div/div['
for i in range(1,5):
        section_xpath = base_xpath + str(i) + ']/div/div/div['

        for j in range(1,8):
                try:
                        xpath = section_xpath + str(j) + ']'
                        item = menu.find_element("xpath", xpath)
                        name = item.find_element("xpath", xpath + '/h5').text

                        print(name)

                except NoSuchElementException:
                        break

                try:
                        special = item.find_element("xpath", xpath + '/div[1]/strong').text
                        
                        print(special)
                
                except NoSuchElementException:
                        break






