# Web-crawler
???
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:21:08 2020

@author: User
"""
import requests
from bs4 import BeautifulSoup

data= requests.get('https://www.books.com.tw/web/sys_saletopb/books/02?attribute=30&loc=act_menu_th_46_002')
soup = BeautifulSoup(data.text, 'html.parser')
print(soup.prettify())
'''
print('=========================================')
print(soup.title)
print('=========================================')
print(soup.a)
print('=========================================')
print(soup.a.attrs)
print('=========================================')
print(soup.p.text)
print('=========================================')
print(soup.find('a'))
print('=========================================')
print(soup.find_all('a'))
print('=========================================')
print(soup.find_all('a' , class_ = 'B'))
print('=========================================')
print(soup.find_all('a' , href = "www.google.com"))
'''

print(soup.find('div' , class_ = "type02_bd-a"))

div_items = soup.find_all('div' , class_ = "type02_bd-a")
i = 0
for div_item in div_items:
    print(div_item)
    
    h4 = div_item.find('h4')
    print(h4.text)
    
    li_price = div_item.find("li" , class_ = "price_a")
    print(li_price.text)
    print('=========================================')
    i = i + 1
    if i > 30:
        break
