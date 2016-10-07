# -*- coding: utf-8 -*- 
import sys
import requests
import codecs
from lxml import html
import sqlite3
#(u'/rs/rent/2016-01/40839.shtml',)
#encoded = [[s.encode('utf8') for s in t] for t in resultsList]

reload(sys)
sys.setdefaultencoding('utf-8')

sqlite_file = 'montreal.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


base = 'http://www.iu91.com'

conn.text_factory = bytes
plinks = c.execute("select link from plinks where id<20")
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
    
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #wrent = " ".join(rent[1].split())
    #.//*[@id='detailpage_left_side']/div[1]/ul/li[3]/span 
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
        #if u'每月租金' in tt[0]:
          # wrent =  " ".join(pp[1].split())
   
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #desc
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #oname
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #phone
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #email
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #print title[0]
    #print waddress
    #print wrent
    #print rstyle[1],method[1],rooms[1],length[1],intime[1]
    #print wstyle,wmethod,wrooms,wlength,wintime,wtenant,wcondition,wequip,wenv
    
    rentsale = tree.xpath('//div[@class="title"]/span[1]/text()')
    #print rentsale
    house = tree.xpath('//div[@class="title"]/span[2]/text()')
    
    if u'出租' in rentsale:
       print 'for rent: ',rentsale[0]
       if u'住宅' in house:
          print 'house:',house[0]
          c.execute('insert into rentinfo ("title","address","rent","rstyle","method","rooms","length","intime","condition","equip","env","metro") values (?,?,?,?,?,?,?,?,?,?,?,?)',(title[0],waddress,wrent,wstyle,wmethod,wrooms,wlength,wintime,wcondition,wequip,wenv,wmetro)) 
conn.commit()  
conn.close()
