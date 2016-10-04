import sqlite3

conn = sqlite3.connect('montreal.sqlite')
c = conn.cursor()

c.execute()


CREATE TABLE "pagelinks" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "link" CHAR)
