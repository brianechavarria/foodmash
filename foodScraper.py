import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

base = "https://dining.columbia.edu/"

url = base 
response = requests.get(url)
soup = BeautifulSoup(response.text, features="lxml")