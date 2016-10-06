# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *

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

#rlink = parser.xpath('//*[@id="listArea"]/ul/li[1]/div/div[2]/div[1]/span/a/text()')
#print rlink[0]
rlink = parser.xpath('//*[@id="listArea"]/ul/li[1]/div/div[2]/div[1]/span/a/@href')
print rlink[0]
utime = parser.xpath('//*[@id="listArea"]/ul/li[1]/div/div[2]/div[5]/text()')
print utime[0]
udate = ''
today = datetime.now()
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
     
res =driver.find_element_by_xpath("//*[@id='listArea']/ul/li[1]/div/div[2]/div[1]/span/a").click()

driver.close()
