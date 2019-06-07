# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:52:08 2018

@author: jd2383
"""

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Main_Page"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, 'html.parser')

txt = soup.get_text()
print(txt)