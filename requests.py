# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
url = "https://search.books.com.tw/search/query/key/%E8%A9%A9%E9%AD%82/cat/all/fclick/autocomp"
data = requests.get(url)
print(data.text)