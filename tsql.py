# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import *
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import codecs
from lxml import html
import sqlite3
import re
from random import randint

sqlite_file = "montreal.sqlite"
conn = sqlite3.connect(sqlite_file)
conn.text_factory = bytes
c = conn.cursor()

murl = 'http://www.iu91.com/rs/rent'

#c.execute("SELECT EXISTS(SELECT 1 FROM airports WHERE ICAO='EHAM')")
num = '45685'

c.execute("SELECT EXISTS(SELECT 1 FROM monrent  WHERE num= %s)" % num)
if c.fetchone():
    print("Found!")

else:
    print("Not found...")
