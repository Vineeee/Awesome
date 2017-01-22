import sys
import MySQLdb

sql = "SELECT * FROM INFOLEGALE_DIRIGEANT;";
conn = MySQLdb.connect( host="localhost",user="root",passwd="Oub@ben123",db="vince",port=3306)
curs = conn.cursor()

try:
    curs.execute(sql)
    rows = curs.fetchall()
except MySQLdb.Error, e:
    try:
        print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
    except IndexError:
        print "MySQL Error: %s" % str(e)
# Print results in comma delimited format
for row in rows:
    for col in row:
        #print "%s," % col
	sys.stdout.write(" %s, " %col)
print ""
