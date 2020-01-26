#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:07:54 2020
 
@author: wuqirong
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
 
chromedriver = "/usr/local/bin/chromedriver"
 
opts = Options()
opts.add_argument("--incognito")  # 使用無痕模式。用 selenium開瀏覽器已經很乾淨了，但疑心病重的可以用一下
 
driver = webdriver.Chrome(chromedriver, chrome_options=opts)
 
driver.get("https://www.books.com.tw")
time.sleep(30)
while(True):
    try:
        driver.get("https://www.books.com.tw/products/0010846042?loc=P_0039_001")
       
        time.sleep(0.5)
        ul = driver.find_element_by_css_selector("ul.btn li:last-child")
        ul.click()
       
        driver.find_element_by_css_selector("a.bt_orange").click()
        time.sleep(1)
       
        driver.find_element_by_css_selector("#t_sm5").click()
        driver.find_element_by_css_selector("label[for='pm01']").click()
        driver.find_element_by_css_selector("a#NextOne").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button#NextOne").click()
       
        print("成功")
    except:
        time.sleep(0.5)
        print("error")