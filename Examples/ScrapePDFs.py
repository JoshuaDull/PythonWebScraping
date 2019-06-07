# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:44:13 2018

@author: jd2383
"""

import csv, requests
from bs4 import BeautifulSoup

with open('caseLawLinks.csv', 'r') as inFile:
    read = csv.reader(inFile)
    for row in read:
        #print(row)
        url = row[1]
        caseName = row[0]
        #print(url, caseName)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        pdf = soup.find('a', class_='pdf-icon')
        #print(pdf)
        pdfLink = 'https:' + pdf['href']
        #print(pdfLink)
        with open(caseName + '.pdf', 'wb') as outFile:
            r2 = requests.get(pdfLink)
            outFile.write(r2.content)