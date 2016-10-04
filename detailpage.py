import requests
import codecs
from lxml import html
import sqlite3
#(u'/rs/rent/2016-01/40839.shtml',)
#encoded = [[s.encode('utf8') for s in t] for t in resultsList]
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
    
    #rent = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[1]/text()')
    #wrent = " ".join(rent[1].split())
    #rstyle = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[2]/text()')
    #wstyle = " ".join(rstyle[1].split())
    #method = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[3]/text()')
    #wmethod = " ".join(method[1].split())
  #.//*[@id='detailpage_left_side']/div[1]/ul/li[3]/span 
    for item in tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li'):
        tt = item.xpath('./span/text()')
        print tt[0]
        pp = item.xpath('./text()')
        print pp[0]
        print 'this is 01'
        print pp[1] 
    #nearby = tree.xpath('//div[@id="detailpage_left_side"]/div[1]/ul/li[12]/text()')
    #wnearby = " ".join(nearby[1].split())
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
    #c.execute('insert into pageinfo ("title") values (?)',(title[0],)) 
conn.commit()  
conn.close()
