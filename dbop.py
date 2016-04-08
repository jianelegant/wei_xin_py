import sqlite3
import accountbean

DB_NAME = "wechat.db"

TABLE_NAME = "publicAccount"
COLUMN_NAME_CHLID = "chlid"
COLUMN_NAME_CHLNAME = "chlname"
COLUMN_NAME_ICON = "icon"
COLUMN_NAME_SICON = "sicon"
COLUMN_NAME_DESC = "desc"
COLUMN_NAME_SUBCOUNT = "subCount"
COLUMN_NAME_KEYWORDS = "keywords"
COLUMN_NAME_UIN = "uin"
COLUMN_NAME_INTRO = "intro"
COLUMN_NAME_RECOMMEND = "recommend"
COLUMN_NAME_WECHAT = "wechat"
COLUMN_NAME_READCOUNT = "readCount"
COLUMN_NAME_SHARECOUNT = "shareCount"
COLUMN_NAME_COLCOUNT = "colCount"

def createTable():
	conn = sqlite3.connect(DB_NAME)

	strCreate = "create table if not exists " + TABLE_NAME \
       + "(" + COLUMN_NAME_CHLID + " varchar primary key not null," \
	   + COLUMN_NAME_CHLNAME + " varchar, " \
	   + COLUMN_NAME_ICON + " varchar, " \
	   + COLUMN_NAME_SICON + " varchar, " \
	   + COLUMN_NAME_DESC + " varchar, " \
	   + COLUMN_NAME_SUBCOUNT + " integer, " \
	   + COLUMN_NAME_KEYWORDS + " varchar, " \
	   + COLUMN_NAME_UIN + " varchar, " \
	   + COLUMN_NAME_INTRO + " varchar, " \
	   + COLUMN_NAME_RECOMMEND + " varchar, " \
	   + COLUMN_NAME_WECHAT + " varchar, " \
	   + COLUMN_NAME_READCOUNT + " integer, " \
	   + COLUMN_NAME_SHARECOUNT + " integer, " \
	   + COLUMN_NAME_COLCOUNT + " integer);"

	print(strCreate)
	conn.execute(strCreate)

	conn.commit()
	conn.close()

def insertItem(acct):
	conn = sqlite3.connect(DB_NAME)
	
	strInsert = "insert into " + TABLE_NAME + " values('" \
		+acct.chlid+"','" \
		+acct.chlname+"','" \
		+acct.icon+"','" \
		+acct.sicon+"','" \
		+acct.desc+"'," \
		+str(acct.subCount)+",'" \
		+acct.keywords+"','" \
		+acct.uin+"','" \
		+acct.intro+"','" \
		+acct.recommend+"','" \
		+acct.wechat+"'," \
		+str(acct.readCount)+"," \
		+str(acct.shareCount)+"," \
		+str(acct.colCount)+");"
	conn.execute(strInsert)
	print(acct.chlid)
	conn.commit()
	conn.close()