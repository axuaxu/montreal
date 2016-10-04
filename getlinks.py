import requests
import codecs
from lxml import html
import sqlite3

sqlite_file = 'montreal.sqlite'
tlink = 'tlink'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor


base = 'http://www.iu91.com/content/listRS?page='

for i in range(2,4):
    murl = base + str(i)
    r = requests.get(murl)
    fname = 'page_'+str(i)+'.html'
    f= codecs.open(fname,'w',encoding='utf8')
    f.write(r.text)
    f.close()
    tree = html.fromstring(r.content)
    rlinks = tree.xpath('//span[@class="title_move"]/a/@href')

print rlinks
print len(rlinks)
