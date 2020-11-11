#! /usr/bin/python3

from selenium import webdriver
import seaborn as sns
import pandas as pd
from datetime import datetime
import requests
import time

url = 'https://www.exploit-db.com/'

browser = webdriver.Firefox()
browser.get(url)
time.sleep(5)
element = browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/thead/tr/th')
elements =browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td')

len(element)
len(elements)

for e in elements :
    print(e.text)

print('END')
