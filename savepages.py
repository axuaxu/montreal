import requests
import codecs

base = 'http://www.iu91.com/content/listRS?page='

for i in range(1,40):
    murl = base + str(i)
    r = requests.get(murl)
    fname = 'page_'+str(i)
    f= codecs.open(fname,'w',encoding='utf8')
    f.write(r.text)
    f.close()

