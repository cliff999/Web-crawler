# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:56:42 2020

@author: User
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.support.ui import Select

chrome = webdriver.Chrome()
chrome.get("https://airtw.epa.gov.tw/")
time.sleep(3)

selectCounty = Select(chrome.find_element_by_id('ddl_county'))
selectCounty.select_by_index(5)
time.sleep(1)
selectSite = Select(chrome.find_element_by_id('ddl_site'))
selectSite.select_by_index(0)
time.sleep(1)
Aquval = chrome.find_element_by_class_name('aquval')
time.sleep(1)


soup = BeautifulSoup(chrome.page_source, "html.parser")
air_info = soup.find_all('div',class_ = 'info')[0]
state = air_info.find('h4').text[:6]
date = air_info.find('div', class_ = 'date').text.strip()[:16]
PM25 = int(air_info.find('span', id = 'PM25').text)
air_quality = air_info.find('b', class_ = 'aquval').text.strip()[:16]
air_quanlity =  'PM25 =' +str(PM25)


webhook_key = '-rd8TxhL8EQEIQ8qU9tPu'
trigger_name = '懸浮粒子'
url = 'https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1={}&value2={}&value3={}'.format(date,state,air_quality,air_quanlity)
requests.get(url)
print(date,state,air_quality,air_quanlity0)