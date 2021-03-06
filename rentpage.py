# -*- coding: utf-8 -*- 
import sys
import re
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

wrent = ''
wstyle =''
wmethod = ''
wcircle = ''
wrooms = ''
wlength = ''
wintime = ''
wcondition = ''
wequip = ''
wenv = ''
wmetro = ''
wtenant = ''
wname = ''

conn.text_factory = bytes
plinks = c.execute("select link from plinks where id<3000")
rows = plinks.fetchall()
for plink in rows:
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
    if u'sale' in purl:
       print 'sales:',purl
       continue
    if not u'2016-10' in purl:
       print 'not 2016-10:',purl
       continue
    r = requests.get(purl)
    tree = html.fromstring(r.content)
    title = tree.xpath('//span[@class="detail_top_title_text"]/text()')
    address = tree.xpath('//div[@class="detailinfosubtitle"]/text()')
    waddress = " ".join(address[0].split())
    
    for item in tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li'):
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
        if u'附属设施' in tt[0]:
           wequip =  " ".join(pp[1].split())
        if u'周边环境' in tt[0]:
           wenv =  " ".join(pp[1].split())
        if u'附近地铁' in tt[0]:
           wmetro =  " ".join(pp[1].split())
   
    ldesc = tree.xpath('//div[@id="summary"]/text()')
    j  = 0
    desc = ''
    while j<len(ldesc):
         desc = desc + ldesc[j]
         j= j+1
    
    oname = tree.xpath('//div[@class="detail_agent_companyname"]/span/text()')
    try:
       wname = oname[0]
    except IndexError:
       wname = ''    
    #email
    phone = tree.xpath('//div[@class="detail_agent_phone"]/span[1]/text()')
    email = tree.xpath('//div[@class="detail_agent_emali"]/a/text()')
    sphone = str(phone)
    semail = str(email)
    sphone = sphone.replace('[','')
    sphone = sphone.replace(']','')
    sphone = sphone.replace("'","",2)
  
    semail = semail.replace('[','')
    semail = semail.replace(']','')
    semail = semail.replace("'","",2)
    print sphone,semail
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
          c.execute('insert into rentpage ("title","address","rent","rstyle","method","rooms","length","intime","condition","equip","env","metro","desc","oname","phone","email","tenant") values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (title[0],waddress,wrent,wstyle,wmethod,wrooms,wlength,wintime,wcondition,wequip,wenv,wmetro,desc,wname,sphone,semail,wtenant)) 
          conn.commit()  
conn.close()
