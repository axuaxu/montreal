# -*- coding: utf-8 -*-

import re
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
import time


areas = ['','','']
print areas
areas[2]='montreal'
print areas

today = str(datetime.now())[:10]
s = '3天前更新'
m = re.search("\d",s)
#if m:
#   tm = m.group(1)
#   print tm
#   udate = str(today+relativedelta(days=-int(m)))[:10]
#   print udate

try:
   found = re.findall('\d+',s)
   ff = int(found[0])
except AttributeError:
   ff = 0
print -ff

