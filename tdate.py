# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
import re

a = u'当天'
print a

if a==u'当天':
   print str(datetime.now())


today = str(datetime.now())[:10]
print today,'='
 
tdate = today[-2:]
yesdate  = int(tdate)-1
bdate = int(tdate)-2

if yesdate < 10:
   yesdate = '0'+str(yesdate)
print tdate,yesdate,bdate

####
today =  datetime.now()
print today
print today+relativedelta(days=-1)


#a='adff 1231 123123kjjksd asdfasd 12123'

#a = 'sfa afakj sdfakjf'

a = '234 234 090'
word1 = " ".join(re.findall("[a-zA-Z]+", a))
sw = ''.join(word1)
num1 = " ".join(re.findall("\d+", a))
sn = ''.join(num1)
print a,word1,num1
print sw,sn
