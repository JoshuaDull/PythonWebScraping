# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:52:08 2018

@author: jd2383
"""

import requests, csv
from bs4 import BeautifulSoup

url = "http://web.library.yale.edu"
r = requests.get(url)
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)

tableData = soup.find_all('td', class_='hours-col-loc')
#print(tableData)

with open('yaleLibraryHours.csv', 'w', newline='') as csvData:
    w = csv.writer(csvData)
    w.writerow(['Library Name','Hours'])    
    for td in tableData:
        libraryName = td.a.text
        hours = td.next_sibling.text
        print(libraryName,hours)
        w.writerow([libraryName,hours])