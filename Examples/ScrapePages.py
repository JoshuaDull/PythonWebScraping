# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:52:08 2018

@author: jd2383
"""
import requests
from bs4 import BeautifulSoup

recPointer = 0

while recPointer <= 150:
	url = "http://orbis.library.yale.edu/vwebv/search?searchArg=raspberry&searchCode=GKEY%5E*&searchType=0&recCount=50&recPointer="+str(recPointer)
	r = requests.get(url)
	#print(r)
	recPointer += 50
	soup = BeautifulSoup(r.text, 'html.parser')
	searchResults = soup.find_all('div', class_="resultListTextCell")

	for item in searchResults:
		info = [item.a.text]
		print(info)