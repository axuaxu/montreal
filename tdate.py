# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *


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

