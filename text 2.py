# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:44:27 2020
@author: User
"""

import time
from selenium import webdriver
import requests
chrome = webdriver.Chrome()

chrome.get('https://www.dcard.tw/f/pet')
chrome.maximize_window()
for i in range(5):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(20)
num = 0
for element in chrome.find_elements_by_class_name("t5f2fb-0.McoWn.sc-1v1d5rx-8.cClYde"):
    img_url = element.get_attribute('src')
    imgRespond = requests.get(img_url)
    print(img_url)
    with open("image\\" + str(num)+".jpg","bw") as file:
        file.write(imgRespond.content)
        num+= 1
    if num > 20:
        break
    
chrome.close()