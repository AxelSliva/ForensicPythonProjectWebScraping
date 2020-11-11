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
elements = browser.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td')

len(element)
len(elements)

for e in elements :
    print(e.text)

res=[]
for i in range ( 0, len(elements),8):
    Date = elements[i].text
    D = elements[i +1].text
    A = elements[i +2].text
    V = elements[i +3].text
    Title = elements[i +4].text
    Type = elements[i +5].text
    Platform = elements[i +6].text
    Author = elements[i +7].text
    res.append((Date,D,A,V,Title,Type,Platform,Author))
res

df = pd.DataFrame (res, columns= ['Date','D','A','V','Title','Type', 'Platform', 'Author'])
df

browser.close()
