#!/usr/bin/python
import MySQLdb
import sys
##script to alert from nagios plugin with simple mysql-python 

def read_db():
    db = MySQLdb.connect("localhost","youruser","yourpassword","yourdbname")
    cursor = db.cursor()
    sql = "SELECT total FROM ccu"

    try:
        cursor.execute(sql)
        results = cursor.fetchone()
	if results != None:
	    result = results
	else:
	    result = 0
	return result
    except Exception, ex:
        print ex
    db.close()

def check():
    ccu = read_db()
    if ccu < warn:
        print "OK - %s Current Users." % ccu
        sys.exit(0)
    elif ccu >= warn:
        print "WARNING - %s Current Users." % ccu
        sys.exit(1)
    elif ccu > crit:
        print "CRITICAL - %s Current Users." % ccu
        sys.exit(2)
    else:
        print "UKNOWN - %s Current Users." % ccu
        sys.exit(3)

if __name__ == '__main__':
    warn = 1500
    crit = 1800
    check()
    #print read_db()

