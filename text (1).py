# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:35:01 2020

@author: User
"""

import json
from bs4 import BeautifulSoup
import requests
data = requests.get("https://www.books.com.tw/web/sys_saletopb/books/02?attribute=30")
soup = BeautifulSoup(data.text, "html.parser")



books_data=[]
index = 0
for info in soup.find_all('div' , class_='type02_bd-a'):
    each_info={}
    name = info.find('h4').text
    author = info.find_all('ul' , class_= 'msg')
    prize = info.find_all('li' , class_= 'prize_a')
    index = index + 1
    print(info)
    print("=============================")
    
    
    

   
    each_info['name'] = name
    each_info['author'] = author
    each_info['prize'] = prize
    books_data.append(each_info)
    
fileName = "books.json"
fp = open(fileName, "w")
json.dump(books_data, fp)
fp.close()