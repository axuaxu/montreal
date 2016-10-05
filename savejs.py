import codecs
import requests
from lxml import html 

#base = 'http://www.iu91.com/content/listRS?page='
    
#for i in range(1,40):

base = 'http://www.iu91.com'
murl = base+'/rs/rent'
r = requests.get(murl)
tree = html.fromstring(r.content)
jslinks = tree.xpath('//script/@src')
for jslink in jslinks:
    if jslink[-2:] =='js':
       print base+jslink
       fn = jslink.rindex('/')+1
       fname = jslink[fn:]
       f= codecs.open(fname,'w',encoding='utf8')
       f.write(r.text)
       f.close()

