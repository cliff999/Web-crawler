# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:31:13 2020

@author: User
"""
import requests
from bs4 import BeautifulSoup

postData = {"startStation": "977abb69-413a-4ccf-a109-0272c24fd490",
"endStation": "a7a04c89-900b-4798-95a3-c01c455622f4",
"theDay": "2020/05/03",
"timeSelect": "10:00",
"waySelect": "DepartureInMandarin",}

res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResult", data = postData)

print(res.text)

soup = BeautifulSoup(res.text, "html.parser")

carNumberList = soup.find_all("div", "ui-block-a")
carTimeList = soup.find_all("div", "ui-block-b")
carFreeList = soup.find_all("div", "ui-block-c")

for i in range(len(carFreeList)):
    print(str(carNumberList[i].text) + 
    "," + str(carTimeList[i]. text) + 
    "," + str(carFreeList[i]. text))
    
print(carFreeList)