# -*- coding: utf-8 -*- 
import sys
import requests
import codecs
from lxml import html
import sqlite3

reload(sys)
sys.setdefaultencoding('utf-8')

sqlite_file = 'montreal.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


base = 'http://www.iu91.com'

conn.text_factory = bytes
plinks = c.execute("select link from plinks where id=100")
for plink in plinks:
    slink  = str(plink)
    llink = list(slink)
    i = llink.index("(")
    del(llink[i])
    i = llink.index(")")
    del(llink[i])
    i = llink.index("'")
    del(llink[i])
    i = llink.index("'")
    del(llink[i])
    i = llink.index(",")
    del(llink[i])
    slink =  ''.join(llink)
    slink.replace("h","")
    purl = base+ slink
    print purl
    r = requests.get(purl)
    tree = html.fromstring(r.content)
    title = tree.xpath('//span[@class="detail_top_title_text"]/text()')
    address = tree.xpath('//div[@class="detailinfosubtitle"]/text()')
    waddress = " ".join(address[0].split())
    
    for item in tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li'):
        tt = item.xpath('./span/text()')
        print tt[0]
        pp = item.xpath('./text()')
        #print pp[0]
        #print pp[1] 
        
        #detail = " ".join((tt[0]+pp[1]).split())
        #print detail
        #if '每月租金'.decode('latin1').encode('utf8') in tt[0]:
        if u'每月租金' in tt[0]:
           wrent =  " ".join(pp[1].split())
           #print 'rent is ', wrent
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
        if u'使用条件' in tt[0]:
           wcondition =  " ".join(pp[1].split())
        if u'附属设施' in tt[0]:
           wequip =  " ".join(pp[1].split())
        if u'周边环境' in tt[0]:
           wenv =  " ".join(pp[1].split())
        if u'附近地铁' in tt[0]:
           wmetro =  " ".join(pp[1].split())
    
        #html/body/div[5]/div[1]/div/div[1]/span[2]
        rentsale = tree.xpath('html/body/div[5]/div[1]/div/div[1]/span[1]')
        if u'出租' in rentsale:
           print 'for rent: ',rentsale

        c.execute('insert into pageinfo ("title","address","rent","rstyle","method","rooms","length","intime","condition","equip","env","metro") values (?,?,?,?,?,?,?,?,?,?,?,?)',(title[0],waddress,wrent,wstyle,wmethod,wrooms,wlength,wintime,wcondition,wequip,wenv,wmetro)) 
#conn.commit()  
conn.close()
