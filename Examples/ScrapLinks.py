# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:52:08 2018

@author: jd2383
"""

import requests, csv
from bs4 import BeautifulSoup

url = 'https://law.justia.com/cases/federal/district-courts/connecticut/ctdce/2018/'

r = requests.get(url)
#print(r)

soup = BeautifulSoup(r.text, 'html.parser')

cases = soup.find_all('a', class_='case-name')
#print(cases)

with open('caseLawLinks.csv', 'w', newline='') as outFile:
    w = csv.writer(outFile)
    for case in cases:
        caseName = case.strong.span.text
        link = 'https://law.justia.com' + case['href']
        #print(link, caseName)
        w.writerow([caseName,link])
       
