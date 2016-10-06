# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import codecs
from lxml import html
import sqlite3
import re

murl = 'http://www.iu91.com/rs/rent'

driver = webdriver.Firefox()
driver.get(murl)
#assert "Python" in driver.title
elem = driver.find_element_by_class_name("showSwitcher")
#elem.clear()
elem.send_keys("QC")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source

parser = html.fromstring(driver.page_source,driver.current_url)

today = datetime.now()
udate = ''
base = 'http://www.iu91.com'

for i in range(3,5):
    
    for j in range(15,17):
        xlink = '//*[@id="listArea"]/ul/li['+str(j)+']/div/div[2]/div[1]/span/a/@href'
        rlink = parser.xpath(xlink)
        print j,rlink[0]
        xtime = '//*[@id="listArea"]/ul/li['+str(j)+']/div/div[2]/div[5]/text()'
        utime = parser.xpath(xtime)
        print utime[0]
        if u'当天更新' in utime[0]:
           udate = str(today)[:10]
        if u'昨天更新' in utime[0]:
           udate = str(today+relativedelta(days=-1))[:10]
        if u'前天更新' in utime[0]:
           udate = str(today+relativedelta(days=-2))[:10]
        m = re.search("\d",utime[0])
        if m:
           udate = str(today+relativedelta(days=-int(m)))[:10]
        print udate

        second_driver = webdriver.Firefox()    
        second_driver.get(base+rlink[0])

        second_parser = html.fromstring(driver.page_source,driver.current_url)
          
        second_driver.close()
 
    time.sleep(10)
    #.//*[@id='pagination']/a[4]
    xpage = '//*[@id="pagination"]/a['+str(i+2)+']/@href'
    rpage = parser.xpath(xpage)
    print i,'next page',rpage[0]    
   
    #driver.get(base+rpage[0])

    #elem = driver.find_element_by_class("nextPage")
    driver.find_element_by_xpath(".//*[@id='pagination']/a[16]").click()
    time.sleep(10)
    parser = html.fromstring(driver.page_source,driver.current_url)
driver.close()
