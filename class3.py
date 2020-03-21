# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:47:27 2020

@author: User
"""

import requests
from bs4 import BeautifulSoup
data = requests.get("https://movies.yahoo.com.tw/movie_thisweek.html")
soup = BeautifulSoup(data.text, "html.parser")

divs = soup.find_all('div' , class_= "release_foto")

for index,ele in enumerate(divs):
    #print(ele)
    #print("=============================")
    img = ele.find('img')
    if not img:
        continue
    #print(str(index + 1) + " : " + img.get("src"))
    img_url = img.get("src")
    #print("=============================")
    
    img_data = requests.get(img_url)
    #print(img_data.content)
    
    fileName = str(index) + ".jpg"
    file = open(fileName, "bw")
    file.write(img_data.content)
    file.close()
    