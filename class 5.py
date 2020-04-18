# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:34:25 2020

@author: user
"""

import requests, json

res = requests.get('https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=40&before=233443183')
data = json.loads(res.text)
print(data)

with open("test.json" , "w")as file:
    json.dump(data, file)
for item in data:
    print(item.get("title"))
    print(item.get("gender"))
    print(item.get("school"))
    print(item.get("topics"))
file.close()
with open("test.json", "r") as file:
    jsonRead = json.load(file)

file.close()