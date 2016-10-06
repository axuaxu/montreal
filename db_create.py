import sqlite3

conn = sqlite3.connect('montreal.sqlite')
c = conn.cursor()

c.execute()


CREATE TABLE "pagelinks" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "link" CHAR)


CREATE TABLE "pageinfo" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "oname" CHAR, "phone" CHAR, "email" CHAR)


CREATE TABLE "rentinfo" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "oname" CHAR, "phone" CHAR, "email" CHAR, "tenant" CHAR, "condition" CHAR, "equip" CHAR, "env" CHAR, "nearby" CHAR, "metro" CHAR)

CREATE TABLE "rentpage" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "oname" CHAR, "phone" CHAR, "email" CHAR, "tenant" CHAR, "condition" CHAR, "equip" CHAR, "env" CHAR, "nearby" CHAR, "metro" CHAR)


CREATE TABLE "monrent" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "num" INTEGER, "udate" CHAR, "rlink" CHAR,"title" CHAR, "address" CHAR, "rent" CHAR, "rstyle" CHAR, "method" CHAR, "rooms" CHAR, "length" CHAR, "intime" CHAR, "desc" TEXT, "tenant" CHAR, "treq" CHAR, "condition" CHAR, "equip" CHAR, "env" CHAR, "bus" CHAR, "metro" CHAR, "hway" CHAR, "oname" CHAR, "phone" CHAR,  "phone2" CHAR, "email" CHAR,"wechat" CHAR,"qq" CHAR )

