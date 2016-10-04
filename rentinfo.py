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
    #stitle = str(title).decode('utf-8')
    #dtitle = stitle.decode('gb18030').decode('utf-8')
    print title[0]
    
    c.execute('insert into pageinfo ("title") values (?)',(title[0],)) 
conn.commit()  
conn.close()
