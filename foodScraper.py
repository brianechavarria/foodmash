import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

urls = ["https://dining.columbia.edu/content/john-jay-dining-hall",
        "https://dining.columbia.edu/content/jjs-place-0",
        "https://dining.columbia.edu/content/ferris-booth-commons-0",
        "https://dining.columbia.edu/chef-mikes",
        "https://dining.columbia.edu/content/faculty-house-0",
        "https://dining.columbia.edu/content/chef-dons-pizza-pi",
        "https://dining.columbia.edu/content/grace-dodge-dining-hall-0",
        "https://dining.columbia.edu/content/fac-shack"]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
