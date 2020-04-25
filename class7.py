# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:44:27 2020

@author: User
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver

chrome = webdriver.Chrome()
chrome.get('https://tw.eztable.com/search/')
time.sleep(3)

chrome.execute_script("window.scrollTo(0, document.body.srollHeight);")
time.sleep(1)


soup = BeautifulSoup(chrome.page_source,"html.parser")
print(soup)

i = 0
for n in range(20):
    for each_prod in soup.find_all('span' ,class_ = "sc-gPzReC gOasMm"):
        productName = each_prod.text
        i = i + 1
        print(str(i) + " : " + str(productName))

i = 0
for a in range(20):
    for each_prod in soup.find_all('h4' ,class_ = "sc-gpHHfC hfPJIb"):
        productName = each_prod.text
        i = i + 1
        print(str(i) + " : " + str(productName))

chrome.quit()
