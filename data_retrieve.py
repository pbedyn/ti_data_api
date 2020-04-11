# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:38:46 2020

@author: pawel
"""

### webscraping packages
import urllib.request, json

url = "https://pbedyn-stores-rest-api.herokuapp.com/stores"

with urllib.request.urlopen(url) as air_data_json:
    df = json.loads(air_data_json.read())