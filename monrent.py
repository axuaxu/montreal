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

def xchar(instr):
    tstr = " ".join(re.findall("[a-zA-Z]+", instr))
    outstr = ''.join(tstr)
    return outstr

def xnum(innum):
    tnum = " ".join(re.findall("\d+", innum))
    outnum = ''.join(tnum)
    return outnum


def setFields(udate,surl,sparser,c):
    num = surl.rsplit('/',1)[1]
    num = num.split('.',1)[0]
    title = sparser.xpath('//span[@class="detail_top_title_text"]/text()')[0]
    #atitle = " ".join(re.findall("[a-zA-Z]+", title[0]))
    atitle = xchar(title)
    tprice = sparser.xpath('//span[@class="detail_top_title_price"]/text()')
    wprice = " ".join(tprice[0].split())
    lprice = wprice.replace(',','')
    aprice = xnum(lprice)
    #rprice = re.findall('\d+',lprice)
    #try:
    #   aprice = rprice[0]    
    #except IndexError:
    #        aprice = 0

    address = sparser.xpath('//div[@class="detailinfosubtitle"]/text()')
    waddress = " ".join(address[0].split())
    pcode = waddress[-7:]
    for item in sparser.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li'):
        tt = item.xpath('./span/text()')
        if not tt:
           print 'empty list'
           continue
        pp = item.xpath('./text()')
        #print pp[1] 
        try:
            detail = " ".join((tt[0]+pp[1]).split())
            #print detail
        except IndexError:
            continue
        if u'每月租金' in tt[0]:
           wrent =  " ".join(pp[1].split())
        if u'房屋类型' in tt[0]:
           wstyle =  " ".join(pp[1].split())
        if u'出租方式' in tt[0]:
           wmethod =  " ".join(pp[1].split())
        if u'周边信息' in tt[0]:
           wcircle =  " ".join(pp[1].split())
        if u'出租房间' in tt[0]:
           wrooms =  " ".join(pp[1].split())
        if u'租约长短' in tt[0]:
           wlength =  " ".join(pp[1].split())
        if u'入住时间' in tt[0]:
           wintime =  " ".join(pp[1].split())
        if u'出租对象' in tt[0]:
           wtenant =  " ".join(pp[1].split())
        if u'使用条件' in tt[0]:
           wcondition =  " ".join(pp[1].split())
        if u'房客要求' in tt[0]:
           wtreq =  " ".join(pp[1].split())
        if u'附属设施' in tt[0]:
           wequip =  " ".join(pp[1].split())
        if u'周边环境' in tt[0]:
           wenv =  " ".join(pp[1].split())
        if u'附近公车' in tt[0]:
           wbus =  " ".join(pp[1].split())
           abus = xnum(wbus)
        ametro = ''
        if u'附近地铁' in tt[0]:
           wmetro =  " ".join(pp[1].split())
           ametro = xchar(wmetro)
        if u'附近火车' in tt[0]:
           wtrain =  " ".join(pp[1].split())
           atrain = xchar(wtrain) 
        if u'附近高速' in tt[0]:
           whway =  " ".join(pp[1].split())
           ahway = xnum(whway)
        ldesc = sparser.xpath('//div[@id="summary"]/text()')
        k  = 0
        desc = ''
        while k<len(ldesc):
            desc = desc + ldesc[k]
            k = k+1

        oname = sparser.xpath('//div[@class="detail_agent_companyname"]/span/text()')
        try:
            wname = oname[0]
        except IndexError:
            wname = ''
        phone = sparser.xpath('//div[@class="detail_agent_phone"]/span[1]/text()')
        email = sparser.xpath('//div[@class="detail_agent_emali"]/a/text()')
        wechat = sparser.xpath('//div[@class="detail_agent_wechat"]/a/text()')
        qq = sparser.xpath('//div[@class="detail_agent_qq"]/a/text()')
        sphone = ''.join(phone)
        semail = ''.join(email)
        swechat = ''.join(wechat)
        sqq = ''.join(qq)
        #sphone = str(phone)
        #semail = str(email)
        #sphone = sphone.replace('[','')
        #sphone = sphone.replace(']','')
        #sphone = sphone.replace("'","",2)

        #semail = semail.replace('[','')
        #semail = semail.replace(']','')
        #semail = semail.replace("'","",2)


    print aprice,pcode,num,title,wprice,atitle,ametro,abus,waddress,wrent,wrooms,wintime,wname,sphone,wechat
    #pass

sqlite_file = "montreal.sqlite"
conn = sqlite3.connect(sqlite_file)
conn.text_factory = bytes
c = conn.cursor()

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

for i in range(1,2):
    
    for j in range(7,9):
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
        surl = base+rlink[0]    
        second_driver.get(surl)

        second_parser = html.fromstring(second_driver.page_source,second_driver.current_url)
        
        setFields(udate,surl,second_parser,c)
  
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
conn.commit()
conn.close()
