import requests
import codecs
from lxml import html
import sqlite3

sqlite_file = 'montreal.sqlite'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()


base = 'http://www.iu91.com'



for i in range(1,3):
    murl = base + str(i)
    r = requests.get(murl)
    tree = html.fromstring(r.content)
    rlinks = tree.xpath('//span[@class="title_move"]/a/@href')
    for rlink in rlinks:
        slink=str(rlink).encode('ascii')
        c.execute('insert into plinks("link") values (?)',(slink,))     
conn.commit()
conn.close()
