import sqlite3
#Dont forget write full way to database file with *.db extention!
sqconn=sqlite3.connect('../errtrackbase.db')
sqcurs=sqconn.cursor()
sqcurs.execute("SELECT * FROM tracker")
for i in sqcurs.fetchall():
    print(i)
sqconn.commit()
sqconn.close()