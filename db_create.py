import sqlite3

conn = sqlite3.connect('montreal.sqlite')
c = conn.cursor()

c.execute()


CREATE TABLE "pagelinks" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "link" CHAR)


CREATE TABLE "pageinfo" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "oname" CHAR, "phone" CHAR, "email" CHAR)


CREATE TABLE "rentinfo" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "oname" CHAR, "phone" CHAR, "email" CHAR, "tenant" CHAR, "condition" CHAR, "equip" CHAR, "env" CHAR, "nearby" CHAR, "metro" CHAR)
