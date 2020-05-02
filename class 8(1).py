# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:44:22 2020

@author: User
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

chrome = webdriver.Chrome()
chrome.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

time.sleep(0.5)
inputBar = chrome.find_element_by_class_name("whsOnd.zHQkBf")

inputBar.send_keys("s1030069@korrnell.hcc.edu.tw")
inputBar.send_keys(Keys.ENTER)
time.sleep(5)

inputBar = chrome.find_element_by_class_name("whsOnd.zHQkBf")
inputBar.send_keys("korrnell2018")
inputBar.send_keys(Keys.ENTER)
time.sleep(5)
'''
i = 0
for element in chrome.find_elements_by_class_name('img-hover'):
    img_url = element.get_attribute('src')
    imgRespond = requests.get(img_url)
    print(i)
    i = i + 1
    if i > 20 :
        break
    file = open(str(i) + ".png", "bw")
    file.write(imgRespond.content)
    file.close()
time.sleep(10) 
'''
chrome.close()