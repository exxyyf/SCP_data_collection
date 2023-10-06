# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:51:21 2023

@author: User
"""



import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

driver = webdriver.Chrome()


url_dict = [{'url':'https://www.bonprix.de/kategorie/herren-mode-t-shirts/?page=',
             'pages':1,
             'category':'t-shirts',
             'i_start':1},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-poloshirts/?page=',
             'pages': 1,
             'category':'poloshirts',
             'i_start': 75},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-tanktops/?page=',
             'pages': 1,
             'category':'tanktops',
             'i_start': 108},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-pullover/?page=',
             'pages': 1,
             'category':'pullover',
             'i_start': 118},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-strickjacken/?page=',
             'pages': 1,
             'category':'strickjacken',
             'i_start': 202},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-herrenjacken/?page=',
             'pages': 1,
             'category':'herrenjacken',
             'i_start': 227},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-maentel/?page=',
             'pages': 1,
             'category':'maentel',
             'i_start': 332},
            
            {'url':'https://www.bonprix.de/kategorie/herren-mode-funktionsjacken/?page=',
             'pages': 1,
             'category':'funktionsjacken',
             'i_start': 339}
            
            
            ]

urls_product = [] 
for m in range(len(url_dict)):            
    url_d = url_dict[m]['url'] 
    category_name = url_dict[m]['category']     
    page_count =  url_dict[m]['pages'] + 1 
     
    for c in range(1, page_count):
        url_shirts = f'{url_d}{c}'                
        driver.get(url_shirts)
        time.sleep(2)  # Allow 2 seconds for the web page to open
        scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1
        
        while True:
            # scroll one screen height each time
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = driver.execute_script("return document.body.scrollHeight;")  
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break 
          
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        link_selector = 'div  div.alpi__content  div.slider__wrapper  div.slider__content-wrapper  div  a'
        for parent in soup.find_all(class_="alpi__image-link"):
            base = 'https://www.bonprix.de'
            link = parent.get("href")
            url_product = urljoin(base, link)
            cat_product = category_name
            product_dict = {}
            product_dict['url'] = url_product
            product_dict['cat'] = cat_product
            urls_product.append(product_dict)
            
            
            
            
#%%
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
import requests
from urllib.request import urlopen, Request
from scrapy import Selector
import pandas as pd
import json
from PIL import Image  
import PIL  
import matplotlib.pyplot as plt
import numpy as np
import os

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

img_links = []
img_titles = []
i=1
for product in urls_product:
    
    request = Request(product['url'], headers=hdr)
    html = urlopen(request).read()
   
    soup = BeautifulSoup(html, 'html.parser')
    obj = soup.find_all('script')[1].text
    obj = json.loads(obj)
    img_url_list = obj['@graph'][1]['image']
    img_links = []
    base_link = 'https://image01.bonprix.de/assets/'
    #base_link = 'https:'
    for url in img_url_list:
        split_url = url.split('//image01.bonprix.de/assets/')
        split2_url = split_url[1].split('/')
        img_size = '687x962/'
        img_links.append(str(base_link + img_size + split2_url[1] + '/' + split2_url[2]))
        #img_links.append(str(base_link + str(url)))
    
    
    paths = ['cloth/', 'person1/', 'person2/', 'person3/', 'person4/', 'person5/']
    if len(img_links) >= 6:
        max_length = 6
    else:
        max_length = len(img_links)
    for x in range(0, max_length):
    
        img = Image.open(urllib.request.urlopen(img_links[x]))
        image_path = str("D:/data/men/upperbody/" + str(paths[x]))
        image = img.save(f"{image_path}{str(i)}_{str(product['cat'])}.jpg")
    print(i)
    i += 1
    