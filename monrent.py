from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import codecs
from lxml import html
import sqlite3

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
print rlink

#driver.find_element_by_xpath("//*[@id='listArea']/ul/li[1]/div/div[2]/div[1]/span/a").click()

driver.close()
