import sqlite3
import datetime
def spreadsheet(linkst):
    edate=(datetime.datetime.now().date())
    etime=(datetime.datetime.now().time())
    #Create database(don't forget write full way to database file with *.db extension!).
    conne=sqlite3.connect('../errtrackbase.db')
    curs=conne.cursor()
    try:
        #Checking for table existence in database
        curs.execute("""CREATE TABLE tracker (
                     evid INTEGER,
                     year INTEGER,
                     month INTEGER,
                     day INTEGER,
                     h INTEGER,
                     minu INTEGER,
                     sec INTEGER,
                     link TEXT)
                     """)
    except:
        pass
    finally:
        pass
    curs.execute("SELECT * FROM tracker")
    #Add +1 to event id cause first row in table has number '0'
    evidn=len(curs.fetchall())+1
    curs.execute("INSERT INTO tracker VALUES (?,?,?,?,?,?,?,?)", 
                 (evidn, edate.year, edate.month, edate.day,
                  etime.hour, etime.minute, etime.second, linkst))
    conne.commit()
    conne.close()
